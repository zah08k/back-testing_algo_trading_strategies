import pandas as pd
import numpy as np
import os.path

pd.options.mode.chained_assignment = None

class Backtest:
    def __init__(self, directory):
        self.directory = directory
        self.file = open("C:/Users/Kubrat/Desktop/Python/" + self.directory + "/" + self.directory + ".txt", "r")
        self.content = self.file.read()
        self.symbols = self.content.split(",")

    def contractdata(self):
        self.data = {}

        for self.symbol in self.symbols:
            if os.path.isfile("C:/Users/Kubrat/Desktop/Python/" + self.directory + "/" + self.symbol + ".csv"):
                df = pd.read_csv("C:/Users/Kubrat/Desktop/Python/" + self.directory + "/" + self.symbol + ".csv",
                                 index_col='date', parse_dates=['date'])
                df['Contract'] = self.symbol
                df['openNextDay'] = df.open.shift(-1)

                self.data[self.symbol] = df[-150:]

        return self.data

class WalkForward:
    def __init__(self):
        pass

    def wf1(self, firstPar, data, train, test, strategy):
        print('wf1 starting')

        self.firstPar = firstPar
        self.data = data
        self.train = train
        self.test = test
        self.strategy = strategy

        score_train = []
        best_score = float('-inf')
        best_firstPar = None

        for parOne in self.firstPar:
            del score_train[:]

            self.trainResults = self.strategy.strat(self.data, self.train, parOne, [], [])

            pnl_sum = self.trainResults.Pnl.sum()
            score_train.append(pnl_sum)

            if sum(score_train) > best_score:
                best_firstPar = parOne
                best_score = sum(score_train)

        self.testResults = self.strategy.strat(self.data, self.test, best_firstPar, [], [])

        print('best par ', best_firstPar)
        print('One test is done')

        return self.testResults

    def wf1filters(self, firstPar, data, train, test, strategy, filters):
        print('wf1 filters starting')

        self.firstPar = firstPar
        self.data = data
        self.train = train
        self.test = test
        self.strategy = strategy

        score_train = []
        best_score = float('-inf')
        best_firstPar = None
        best_filter = None

        # Start the optimization for the train data - find the best parameters and best filters. Start with
        # "for filt in dir(self.filters) because if we start first with "for parOne in self.firstPar" we receive error
        for filt in dir(filters):
            if filt.startswith('__'):
                continue

            for parOne in self.firstPar:
                del score_train[:]

                self.trainResults = self.strategy.strat(self.data, self.train, parOne, filters, filt)

                pnl_sum = self.trainResults.Pnl.sum()
                score_train.append(pnl_sum)

                if sum(score_train) > best_score:
                    best_firstPar = parOne
                    best_filter = filt
                    best_score = sum(score_train)

        print('Best Score: ', best_score)
        self.testResults = self.strategy.strat(self.data, self.test, best_firstPar, filters, best_filter)

        print('- best par ', best_firstPar, 'best filt ', best_filter,' -')
        print('One test is done')

        return self.testResults

class Performance:
    def __init__(self):
        pass
    def performance(self, results):
        self.results = results
        self.results['NetPnl'] = self.results.Pnl.cumsum()
        self.results['RlzdRunningMax'] = np.maximum.accumulate(self.results.NetPnl)
        self.results['RlzdDrawdown'] = self.results.NetPnl - self.results.RlzdRunningMax  # For plot and NewEquityHigh
        self.results['NewEquityHigh'] = np.where(self.results.RlzdDrawdown == 0, self.results.NetPnl, np.nan)

        net_pnl = sum(self.results.Pnl)
        winrate = self.results.Win.sum() / (self.results.Win.sum() + self.results.Loss.sum())
        pr_factor = self.results.Pnl[self.results.Pnl > 0].sum() / abs(self.results.Pnl[self.results.Pnl < 0].sum())
        num_trades = sum(self.results.Win) + sum(self.results.Loss)
        max_win = self.results.Pnl.max()
        max_loss = self.results.Pnl.min()
        avg_win = np.mean(self.results.Pnl[self.results.Pnl > 0])
        avg_loss = np.mean(self.results.Pnl[self.results.Pnl < 0])
        avg_trade = np.mean(self.results.Pnl)
        max_dd = self.results.RlzdDrawdown.min()
        romad = net_pnl / abs(self.results.RlzdDrawdown.min())
        avg_days = self.results.HoldingDays.mean()

        # Find max number of consecutive losses and max consecutive loss value (dollar&euro)
        num_loss_counter = 0
        max_num_cons_loss = 0

        dummy_df = self.results.Pnl.loc[(self.results.Pnl != 0)]
        for i in range(len(dummy_df)):
            if dummy_df[i] < 0:
                num_loss_counter += 1

            else:
                max_num_cons_loss = max(num_loss_counter, max_num_cons_loss)
                num_loss_counter = 0

        self.dfResults = pd.DataFrame(
            data=[net_pnl, winrate, pr_factor, max_dd, romad,
                  num_trades, max_win, max_loss, max_num_cons_loss, avg_win, avg_loss, avg_trade, avg_days],
            index=['Net Pnl', 'Winrate', 'Profit Factor', 'Max Drawdown', 'Romad', 'All Trades',
                   'Max Onetime Profit', 'Max Onetime Loss', 'Max Consec Loss', 'Average Profit per Trade',
                   'Average Loss per Trade', 'Average Pnl per Trade', 'Average Holding'])

        return self.dfResults

