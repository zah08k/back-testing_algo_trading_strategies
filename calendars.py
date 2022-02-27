import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

class Calendar:
    def __init__(self, df):
        self.df = df

    def dayofweek(self):
        self.df['DayOfWeek'] = self.df.index.dayofweek
        return self.df

    def months(self):
        self.df['Month'] = self.df.index.month
        self.df['FDOM'] = np.where(self.df.Month != self.df.Month.shift(1), 1, 0) # First Day Of The Month
        self.df.FDOM = self.df.FDOM.shift(-1)
        return self.df
