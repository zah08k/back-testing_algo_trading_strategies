import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

class Candlesticks:
    def __init__(self, df):
        self.df = df

    def engulfing(self):
        self.df['BullEngulfing'] = np.where((self.df.close.shift(1) < self.df.open.shift(1)) &
                                            (self.df.open < self.df.close.shift(1)) &
                                            (self.df.close > self.df.open.shift(1)) & (
                                                        self.df.low < self.df.low.shift(1)) &
                                            (self.df.high > self.df.high.shift(1)), 1, 0)

        self.df['BearEngulfing'] = np.where((self.df.close.shift(1) > self.df.open.shift(1)) &
                                            (self.df.open > self.df.close.shift(1)) &
                                            (self.df.close < self.df.open.shift(1)) & (
                                                        self.df.low < self.df.low.shift(1)) &
                                            (self.df.high > self.df.high.shift(1)), 1, 0)

        self.df.BullEngulfing = self.df.BullEngulfing.shift(1)
        self.df.BearEngulfing = self.df.BearEngulfing.shift(1)
        return self.df

    def insidebar(self):
        self.df['InsBarOne'] = np.where((self.df.high < self.df.high.shift(1)) & (self.df.low > self.df.low.shift(1)),
                                        1, 0)
        self.df['InsBarTwo'] = np.where((self.df.high.shift(1) < self.df.high.shift(2)) &
                                        (self.df.low.shift(1) > self.df.low.shift(2)) &
                                        (self.df.high < self.df.high.shift(1)) & (self.df.low > self.df.low.shift(1)),
                                        1, 0)

        self.df.InsBarOne = self.df.InsBarOne.shift(1)
        self.df.InsBarTwo = self.df.InsBarTwo.shift(1)
        return self.df

    def spike(self):
        self.df['UpSpike'] = np.where(
            (((self.df.close - self.df.low) / (self.df.high - self.df.low) < 0.30) & (self.df.close >= self.df.open)) |
            (((self.df.open - self.df.low) / (self.df.high - self.df.low) < 0.30) & (self.df.open > self.df.close)), 1,
            0)
        self.df['DownSpike'] = np.where(
            (((self.df.close - self.df.low) / (self.df.high - self.df.low) > 0.70) & (self.df.close <= self.df.open)) |
            (((self.df.open - self.df.low) / (self.df.high - self.df.low) > 0.70) & (self.df.open < self.df.close)), 1,
            0)

        self.df.UpSpike = self.df.UpSpike.shift(1)
        self.df.DownSpike = self.df.DownSpike.shift(1)
        return self.df

    def updownclose(self, window): # Count number of positive vs negative days for a specific lookback period
        self.df['UpDay'] = np.where(self.df.close - self.df.open > 0, 1, 0)
        self.df['DownDay'] = np.where(self.df.open - self.df.close > 0, 1, 0)
        self.df['SignalU'] = np.where(self.df.UpDay.rolling(window).sum() > self.df.DownDay.rolling(window).sum(), 1, 0)
        self.df['SignalD'] = np.where(self.df.UpDay.rolling(window).sum() < self.df.DownDay.rolling(window).sum(), -1, 0)

        self.df['SignalUpDown'] = self.df.SignalU + self.df.SignalD
        self.df.SignalUpDown = self.df.SignalUpDown.shift(1)
        return self.df

    def highlowbars(self, window): # Same as updownbars but look if higher highs are more than lower lows and vice versa
        self.df['HHDay'] = np.where(self.df.high > self.df.high.shift(1), 1, 0)
        self.df['LLDay'] = np.where(self.df.high < self.df.high.shift(1), 1, 0)
        self.df['SignalH'] = np.where(self.df.HHDay.rolling(window).sum() > self.df.LLDay.rolling(window).sum(), 1, 0)
        self.df['SignalL'] = np.where(self.df.HHDay.rolling(window).sum() < self.df.LLDay.rolling(window).sum(), -1, 0)

        self.df['SignalHighLow'] = self.df.SignalH + self.df.SignalL
        self.df.SignalHighLow = self.df.SignalHighlow.shift(1)
        return self.df

    def prevbarsrange(self, window): # Previous bars range. Can be used for momentum trading
        highest_value = self.df.high.rolling(window).max()
        lowest_value = self.df.low.rolling(window).min()
        close_index = (self.df.close - lowest_value) / (highest_value - lowest_value)
        self.df['HRV'] = highest_value # Highest Range Value
        self.df['LRV'] = lowest_value # Lowest Range Value

        self.df['CI'] = close_index # Close Index
        self.df.CI = self.df.CI.shift(1)
        return self.df

    def highestlowest(self,window): # highest high, highest low, highest close, lowest high, lowest, low, lowest close
        hh = np.where(self.df.high.rolling(window).max() == self.df.high, 1, 0)
        hl = np.where(self.df.low.rolling(window).max() == self.df.low, 1, 0)
        hc = np.where(self.df.close.rolling(window).max() == self.df.close, 1, 0)

        lh = np.where(self.df.high.rolling(window).min() == self.df.high, 1, 0)
        ll = np.where(self.df.low.rolling(window).min() == self.df.low, 1, 0)
        lc = np.where(self.df.close.rolling(window).min() == self.df.close,1, 0)

        self.df['HH'] = hh
        self.df['HL'] = hl
        self.df['HC'] = hc

        self.df['LH'] = lh
        self.df['LL'] = ll
        self.df['LC'] = lc

        self.df['HH'] = self.df.HH.shift(1)
        self.df['HL'] = self.df.HL.shift(1)
        self.df['HC'] = self.df.HC.shift(1)

        self.df['LH'] = self.df.LH.shift(1)
        self.df['LL'] = self.df.LL.shift(1)
        self.df['LC'] = self.df.LC.shift(1)
        return self.df

    def ohlcshift(self):
        self.df['openShift'] = self.df.open.shift(1)
        self.df['highShift'] = self.df.high.shift(1)
        self.df['lowShift'] = self.df.low.shift(1)
        self.df['closeShift'] = self.df.close.shift(1)
        return self.df



