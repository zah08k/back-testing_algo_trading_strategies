import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'


class Filters:
    def __init__(self):
        pass

    def ema20(self,df): # Price > Ema(20) is Uptrend
        self.df = df
        ema = self.df.close.ewm(span=20, adjust=False).mean()
        self.df['Ema'] = ema
        self.df['FilterLong'] = np.where(self.df.close > self.df.Ema, 1, 0)
        self.df['FilterShort'] = np.where(self.df.close < self.df.Ema, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)

        return self.df

    def ema40(self,df): # Price > Ema(40) is Uptrend
        self.df = df
        ema = self.df.close.ewm(span=40, adjust=False).mean()
        self.df['Ema'] = ema
        self.df['FilterLong'] = np.where(self.df.close > self.df.Ema, 1, 0)
        self.df['FilterShort'] = np.where(self.df.close < self.df.Ema, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)

        return self.df

    def ema2040(self,df): # EmaFast(20) > EmaSlow(40) is Uptrend and vice versa
        self.df = df
        ema_fast = self.df.close.ewm(span=20, adjust=False).mean()
        ema_slow = self.df.close.ewm(span=40, adjust=False).mean()
        self.df['EmaFast'] = ema_fast
        self.df['EmaSlow'] = ema_slow
        self.df['FilterLong'] = np.where(self.df.EmaFast > self.df.EmaSlow, 1, 0)
        self.df['FilterShort'] = np.where(self.df.EmaFast < self.df.EmaSlow, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)

        return self.df

    def rsi5(self,df): # RSI(5) > 50 momentum is up, RSI < 50 momentum is down
        self.df = df
        up = np.where(self.df.close > self.df.close.shift(1), self.df.close - self.df.close.shift(1), 0)
        down = np.where(self.df.close < self.df.close.shift(1), self.df.close.shift(1) - self.df.close, 0)
        self.df['Up'] = up
        self.df['Down'] = down
        avg_up = self.df.Up.ewm(span=5, adjust=False).mean()
        avg_down = self.df.Down.ewm(span=5, adjust=False).mean()
        rs = avg_up / avg_down
        rsi = 100 - (100 / (1 + rs))
        self.df['Rsi'] = rsi
        self.df['FilterLong'] = np.where(self.df.Rsi > 50, 1, 0)
        self.df['FilterShort'] = np.where(self.df.Rsi < 50, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)
        return self.df

    def rsi10(self,df): # RSI(10) > 50 momentum is up, RSI < 50 momentum is down
        self.df = df
        up = np.where(self.df.close > self.df.close.shift(1), self.df.close - self.df.close.shift(1), 0)
        down = np.where(self.df.close < self.df.close.shift(1), self.df.close.shift(1) - self.df.close, 0)
        self.df['Up'] = up
        self.df['Down'] = down
        avg_up = self.df.Up.ewm(span=10, adjust=False).mean()
        avg_down = self.df.Down.ewm(span=10, adjust=False).mean()
        rs = avg_up / avg_down
        rsi = 100 - (100 / (1 + rs))
        self.df['Rsi'] = rsi
        self.df['FilterLong'] = np.where(self.df.Rsi > 50, 1, 0)
        self.df['FilterShort'] = np.where(self.df.Rsi < 50, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)
        return self.df

    def adx5(self, df): # Adx(5) > 25 is stronger trend
        self.df = df
        plus_dm = self.df.high.diff()
        minus_dm = self.df.low.diff()
        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm > 0] = 0
        tr1 = pd.DataFrame(self.df.high - self.df.low)
        tr2 = pd.DataFrame(abs(self.df.high - self.df.close.shift(1)))
        tr3 = pd.DataFrame(abs(self.df.low - self.df.close.shift(1)))
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis=1, join='inner').max(axis=1)
        atr = tr.rolling(5).mean()
        plus_di = 100 * (plus_dm.ewm(alpha=1 / 5).mean() / atr)
        minus_di = abs(100 * (minus_dm.ewm(alpha=1 / 5).mean() / atr))
        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = ((dx.shift(1) * (5 - 1)) + dx) / 5
        adx_smooth = adx.ewm(alpha=1 / 5).mean()
        self.df['Adx'] = adx_smooth
        self.df['FilterLong'] = np.where(self.df.Adx > 25, 1, 0)
        self.df['FilterShort'] = np.where(self.df.Adx > 25, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)
        return self.df

    def macd12269(self, df):
        self.df = df
        fast = self.df.close.ewm(span=12, adjust=False).mean()
        slow = self.df.close.ewm(span=26, adjust=False).mean()
        macd = fast - slow

        self.df['MACD'] = macd
        self.df['MACDSignal'] = self.df.MACD.ewm(span=9, adjust=False).mean()
        self.df['FilterLong'] = np.where(self.df.MACD > self.df.MACDSignal, 1, 0)
        self.df['FilterShort'] = np.where(self.df.MACD < self.df.MACDSignal, 1, 0)

        self.df.FilterLong = self.df.FilterLong.shift(1)
        self.df.FilterShort = self.df.FilterShort.shift(1)
        return self.df
