import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'


class Indicators:
    def __init__(self, df):
        self.df = df

    def ema(self, ema_n):
        ema = self.df.close.ewm(span=ema_n, adjust=False).mean()

        self.df['Ema'] = ema
        self.df['EmaSignal'] = np.where(self.df.close > self.df.Ema, 1, -1)
        self.df.Ema = self.df.Ema.shift(1)
        self.df.EmaSignal = self.df.EmaSignal.shift(1)
        return self.df

    def emacross(self, ema_f, ema_s):
        ema_fast = self.df.close.ewm(span=ema_f, adjust=False).mean()
        ema_slow = self.df.close.ewm(span=ema_s, adjust=False).mean()
        self.df['EmaFast'] = ema_fast
        self.df['EmaSlow'] = ema_slow

        self.df['EmaCross'] = np.where(self.df.EmaFast > self.df.EmaSlow, 1, -1)
        self.df.EmaCross = self.df.EmaCross.shift(1)
        return self.df

    def rsi(self, window):
        up = np.where(self.df.close > self.df.close.shift(1), self.df.close - self.df.close.shift(1), 0)
        down = np.where(self.df.close < self.df.close.shift(1), self.df.close.shift(1) - self.df.close, 0)
        self.df['Up'] = up
        self.df['Down'] = down
        avg_up = self.df.Up.ewm(span=window, adjust=False).mean()
        avg_down = self.df.Down.ewm(span=window, adjust=False).mean()
        rs = avg_up / avg_down
        rsi = 100 - (100 / (1 + rs))

        self.df['Rsi'] = rsi
        self.df.Rsi = self.df.Rsi.shift(1)
        return self.df

    def atr(self, window):
        self.df['tr1'] = abs(self.df.high - self.df.low)
        self.df['tr2'] = abs(self.df.high - self.df.close.shift(1))
        self.df['tr3'] = abs(self.df.low - self.df.close.shift(1))
        self.df['atr0'] = self.df[['tr1', 'tr2', 'tr3']].max(axis=1)

        self.df['Atr'] = self.df['atr0'].ewm(span=window, adjust=False).mean()
        self.df.Atr = self.df.Atr.shift(1)
        return self.df

    def adx(self, window):
        plus_dm = self.df.high.diff()
        minus_dm = self.df.low.diff()
        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm > 0] = 0
        tr1 = pd.DataFrame(self.df.high - self.df.low)
        tr2 = pd.DataFrame(abs(self.df.high - self.df.close.shift(1)))
        tr3 = pd.DataFrame(abs(self.df.low - self.df.close.shift(1)))
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis=1, join='inner').max(axis=1)
        atr = tr.rolling(window).mean()
        plus_di = 100 * (plus_dm.ewm(alpha=1 / window).mean() / atr)
        minus_di = abs(100 * (minus_dm.ewm(alpha=1 / window).mean() / atr))
        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = ((dx.shift(1) * (window - 1)) + dx) / window
        adx_smooth = adx.ewm(alpha=1 / window).mean()

        self.df['Adx'] = adx_smooth
        self.df.Adx = self.df.Adx.shift(1)
        return self.df

    def bbands(self,window,multiplier):
        middle = self.df.close.ewm(span=window, adjust=True).mean()
        upper = middle + (self.df.close.rolling(window).std() * multiplier)
        lower = middle - (self.df.close.rolling(window).std() * multiplier)

        self.df['Middle'] = middle
        self.df['Upper'] = upper
        self.df['Lower'] = lower
        self.df.Middle = self.df.Middle.shift(1)
        self.df.Upper = self.df.Upper.shift(1)
        self.df.Lower = self.df.Lower.shift(1)
        return self.df

    def macd(self,ema_fast,ema_slow,signal):
        fast = self.df.close.ewm(span=ema_fast, adjust=False).mean()
        slow = self.df.close.ewm(span=ema_slow, adjust=False).mean()
        macd = fast - slow

        self.df['MACD'] = macd
        self.df['MACDSignal'] = self.df.MACD.ewm(span=signal, adjust=False).mean()
        self.df.MACD = self.df.MACD.shift(1)
        self.df.MACDSignal = self.df.MACDSignal.shift(1)
        return self.df

    def emazscore(self,ema_f,ema_s,std_n,z_signal):
        ema_fast = self.df.close.ewm(span=ema_f, adjust=False).mean()
        ema_slow = self.df.close.ewm(span=ema_s, adjust=False).mean()
        ema_diff = ema_fast - ema_slow
        pef_diff = self.df['close'] - ema_fast

        self.df['ema_diff_z'] = (ema_diff - ema_diff.rolling(std_n).mean()) / ema_diff.rolling(std_n).std()
        self.df['pef_diff_z'] = (pef_diff - pef_diff.rolling(std_n).mean()) / pef_diff.rolling(std_n).std()

        # Signals
        self.df['Long_ema'] = np.where(self.df['ema_diff_z'] < -z_signal, 1, 0)
        self.df['Short_ema'] = np.where(self.df['ema_diff_z'] > z_signal, -1, 0)
        self.df['SignalEma'] = self.df['Long_ema'] + self.df['Short_ema']

        self.df['Long_pef'] = np.where(self.df['pef_diff_z'] < -z_signal, 1, 0)
        self.df['Short_pef'] = np.where(self.df['pef_diff_z'] > z_signal, -1, 0)
        self.df['SignalPef'] = self.df['Long_pef'] + self.df['Short_pef']

        self.df.SignalEma = self.df.SignalEma.shift(1)
        self.df.SignalPef = self.df.SignalPef.shift(1)
        return self.df

    def pivotpoints(self):
        pp = (self.df.high + self.df.low + self.df.close) / 3
        r1 = (2 * pp) - self.df.low
        s1 = (2 * pp) - self.df.high
        r2 = pp + (self.df.high - self.df.low)
        s2 = pp - (self.df.high - self.df.low)
        r3 = self.df.high + 2 * (pp - self.df.low)
        s3 = self.df.low - 2 * (self.df.high - pp)

        self.df['PP'] = round(pp, 0)
        self.df['R1'] = round(r1, 0)
        self.df['S1'] = round(s1, 0)
        self.df['R2'] = round(r2, 0)
        self.df['S2'] = round(s2, 0)
        self.df['R3'] = round(r3, 0)
        self.df['S3'] = round(s3, 0)

        self.df.PP = self.df.PP.shift(1)
        self.df.R1 = self.df.R1.shift(1)
        self.df.S1 = self.df.S1.shift(1)
        self.df.R2 = self.df.R2.shift(1)
        self.df.S2 = self.df.S2.shift(1)
        self.df.R3 = self.df.R3.shift(1)
        self.df.S3 = self.df.S3.shift(1)
        return self.df

