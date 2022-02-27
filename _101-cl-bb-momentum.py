import pandas as pd
import numpy as np
import os.path
from datetime import datetime, timedelta
import time
import matplotlib.pyplot as plt

import concurrent.futures
from backtest import *
from contracts import *
from indicators import *
from filters import *
from calendars import *
from candlesticks import *

pd.options.mode.chained_assignment = None
start = time.perf_counter()

class Strategy():
    def __init__(self, fees, slippage, mltp):
        self.fees = fees
        self.slippage = slippage
        self.mltp = mltp

    def strat(self, data, symbols, parOne, filters, filt):
        pm = {'EntryDate': [], 'ExitDate': [], 'EntryPrice': [], 'ExitPrice': [], 'Pnl': [], 'Win': [], 'Loss': [],
              'Trade': [], 'HoldingDays': []}

        for symbol in symbols:
            self.df = data[symbol]

            # If looking for best filters:
            if filters and filt:
                self.df = getattr(filters, filt)(self.df)

            # Indicators, Candlesticks and others
            indicator = Indicators(self.df)
            calendar = Calendar(self.df)
            candlesticks = Candlesticks(self.df)

            self.df = candlesticks.ohlcshift()
            self.df = indicator.bbands(10,1.9)

            # Start:end period, last trading day(Lqdt), max holding time(max_hold)
            startend = StartEnd(symbol)
            start, end = startend.cl()
            self.df = self.df[start:end]

            lqdt = self.df.index[-1]
            self.df['Lqdt'] = np.where(self.df.index == lqdt, True, False)
            self.df['Point'] = range(len(self.df.index))
            max_hold = 4

            # Entry and exit variables
            entry_price = float(0)
            exit_price = float(0)
            entry_date = timedelta(days=0)
            exit_date = None
            entry_day = 0
            inpos = 0

            profit_target = float(0)
            max_profit = 0.25
            stop_loss = float(0)
            max_loss = 500
            limit_entry_diff = parOne

            limit_order = float(0)
            long_entry_order = False
            short_entry_order = False


            # Long
            for i in self.df.index:
                if self.df.highShift[i] > self.df.Upper[i] \
                        and not inpos and not self.df.Lqdt[i]:

                    if self.df.low[i] < self.df.open[i] - limit_entry_diff:
                        entry_price = self.df.open[i] - limit_entry_diff
                        entry_date = i
                        entry_day = self.df.Point[i]

                        profit_target = entry_price + max_profit
                        stop_loss = entry_price - max_loss

                        inpos = 1
                    else:
                        continue

                elif (self.df.high[i] > profit_target or self.df.low[i] <= stop_loss or
                        self.df.Point[i] - entry_day >= max_hold or self.df.Lqdt[i]) and inpos == 1:
                    if self.df.high[i] > profit_target:
                        if self.df.open[i] > profit_target:
                            exit_price = self.df.open[i] - self.slippage
                        else:
                            exit_price = profit_target
                    elif self.df.low[i] <= stop_loss:
                        if self.df.open[i] < stop_loss:
                            exit_price = self.df.open[i] - self.slippage
                        else:
                            exit_price = stop_loss - self.slippage
                    elif self.df.Point[i] - entry_day >= max_hold or self.df.Lqdt[i]:
                        exit_price = self.df.close[i] - self.slippage

                    exit_date = i
                    pnl = ((exit_price - entry_price) * self.mltp) - self.fees
                    win = np.where(pnl > 0, 1, 0)
                    loss = np.where(pnl < 0, 1, 0)

                    pm['EntryDate'].append(entry_date),
                    pm['ExitDate'].append(exit_date),
                    pm['EntryPrice'].append(entry_price),
                    pm['ExitPrice'].append(exit_price),
                    pm['Pnl'].append(pnl),
                    pm['Win'].append(win),
                    pm['Loss'].append(loss)
                    pm['Trade'].append('Long')
                    pm['HoldingDays'].append(self.df.Point[i] - entry_day)

                    inpos = 0

                # Short
                elif self.df.lowShift[i] < self.df.Lower[i] \
                        and not inpos and not self.df.Lqdt[i]:

                    if self.df.high[i] > self.df.open[i] + limit_entry_diff:
                        entry_price = self.df.open[i] + limit_entry_diff
                        entry_date = i
                        entry_day = self.df.Point[i]

                        profit_target = entry_price - max_profit
                        stop_loss = entry_price + max_loss

                        inpos = -1
                    else:
                        continue

                elif (self.df.low[i] < profit_target or self.df.high[i] >= stop_loss or
                      self.df.Point[i] - entry_day >= max_hold or self.df.Lqdt[i]) and inpos == -1:
                    if self.df.low[i] < profit_target:
                        if self.df.open[i] < profit_target:
                            exit_price = self.df.open[i] + self.slippage
                        else:
                            exit_price = profit_target
                    elif self.df.high[i] >= stop_loss:
                        if self.df.open[i] > stop_loss:
                            exit_price = self.df.open[i] + self.slippage
                        else:
                            exit_price = stop_loss + self.slippage
                    elif self.df.Point[i] - entry_day >= max_hold or self.df.Lqdt[i]:
                        exit_price = self.df.close[i] + self.slippage

                    exit_date = i
                    pnl = ((entry_price - exit_price) * self.mltp) - self.fees
                    win = np.where(pnl > 0, 1, 0)
                    loss = np.where(pnl < 0, 1, 0)

                    pm['EntryDate'].append(entry_date),
                    pm['ExitDate'].append(exit_date),
                    pm['EntryPrice'].append(entry_price),
                    pm['ExitPrice'].append(exit_price),
                    pm['Pnl'].append(pnl),
                    pm['Win'].append(win),
                    pm['Loss'].append(loss)
                    pm['Trade'].append('Short')
                    pm['HoldingDays'].append(self.df.Point[i] - entry_day)

                    inpos = 0

        self.dfResults = pd.DataFrame(data=pm)

        return self.dfResults


def main():
    start = time.perf_counter()

    directory = 'cl'
    fees = 3
    slippage = 0.02 # 2 ticks
    multiplier = 1000

    testing_method = 'wf1'

    firstPar = [0.1,0.2,0.3,0.4,0.5]

    timeseries = Backtest(directory)
    traintest = TrainTest()
    data = timeseries.contractdata()
    print('data is ready')

    tr1,te1,tr2,te2,tr3,te3,tr4,te4,tr5,te5,tr6,te6,\
    tr7,te7,tr8,te8,tr9,te9,tr10,te10,tr11,te11,tr12,te12 = traintest.cl()

    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    result7 = []
    result8 = []
    result9 = []
    result10 = []
    result11 = []
    result12 = []

    print('PoolExecutor starting')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        if testing_method == 'wf1':
            walkforward = WalkForward()
            test1 = executor.submit(walkforward.wf1, firstPar, data, tr1, te1, Strategy(fees,slippage,multiplier))
            walkforward = WalkForward()
            test2 = executor.submit(walkforward.wf1, firstPar, data, tr2, te2, Strategy(fees,slippage,multiplier))
            walkforward = WalkForward()
            test3 = executor.submit(walkforward.wf1, firstPar, data, tr3, te3, Strategy(fees,slippage,multiplier))
            walkforward = WalkForward()
            test4 = executor.submit(walkforward.wf1, firstPar, data, tr4, te4, Strategy(fees,slippage,multiplier))
            walkforward = WalkForward()
            test5 = executor.submit(walkforward.wf1, firstPar, data, tr5, te5, Strategy(fees,slippage,multiplier))
            walkforward = WalkForward()
            test6 = executor.submit(walkforward.wf1, firstPar, data, tr6, te6, Strategy(fees,slippage,multiplier))
            walkforward = WalkForward()
            test7 = executor.submit(walkforward.wf1, firstPar, data, tr7, te7, Strategy(fees, slippage, multiplier))
            walkforward = WalkForward()
            test8 = executor.submit(walkforward.wf1, firstPar, data, tr8, te8, Strategy(fees, slippage, multiplier))
            walkforward = WalkForward()
            test9 = executor.submit(walkforward.wf1, firstPar, data, tr9, te9, Strategy(fees, slippage, multiplier))
            walkforward = WalkForward()
            test10 = executor.submit(walkforward.wf1, firstPar, data, tr10, te10, Strategy(fees, slippage, multiplier))
            walkforward = WalkForward()
            test11 = executor.submit(walkforward.wf1, firstPar, data, tr11, te11, Strategy(fees, slippage, multiplier))
            walkforward = WalkForward()
            test12 = executor.submit(walkforward.wf1, firstPar, data, tr12, te12, Strategy(fees, slippage, multiplier))

        elif testing_method == 'wf1filters':
            walkforward = WalkForward()
            test1 = executor.submit(walkforward.wf1filters, firstPar, data, tr1, te1, Strategy(fees,slippage,multiplier), Filters())
            walkforward = WalkForward()
            test2 = executor.submit(walkforward.wf1filters, firstPar, data, tr2, te2, Strategy(fees,slippage,multiplier), Filters())
            walkforward = WalkForward()
            test3 = executor.submit(walkforward.wf1filters, firstPar, data, tr3, te3, Strategy(fees,slippage,multiplier), Filters())
            walkforward = WalkForward()
            test4 = executor.submit(walkforward.wf1filters, firstPar, data, tr4, te4, Strategy(fees,slippage,multiplier), Filters())
            walkforward = WalkForward()
            test5 = executor.submit(walkforward.wf1filters, firstPar, data, tr5, te5, Strategy(fees,slippage,multiplier), Filters())
            walkforward = WalkForward()
            test6 = executor.submit(walkforward.wf1filters, firstPar, data, tr6, te6, Strategy(fees,slippage,multiplier), Filters())
            walkforward = WalkForward()
            test7 = executor.submit(walkforward.wf1filters, firstPar, data, tr7, te7, Strategy(fees, slippage, multiplier), Filters())
            walkforward = WalkForward()
            test8 = executor.submit(walkforward.wf1filters, firstPar, data, tr8, te8, Strategy(fees, slippage, multiplier), Filters())
            walkforward = WalkForward()
            test9 = executor.submit(walkforward.wf1filters, firstPar, data, tr9, te9, Strategy(fees, slippage, multiplier), Filters())
            walkforward = WalkForward()
            test10 = executor.submit(walkforward.wf1filters, firstPar, data, tr10, te10, Strategy(fees, slippage, multiplier), Filters())
            walkforward = WalkForward()
            test11 = executor.submit(walkforward.wf1filters, firstPar, data, tr11, te11, Strategy(fees, slippage, multiplier), Filters())
            walkforward = WalkForward()
            test12 = executor.submit(walkforward.wf1filters, firstPar, data, tr12, te12, Strategy(fees, slippage, multiplier), Filters())

    result1.append(test1.result())
    result2.append(test2.result())
    result3.append(test3.result())
    result4.append(test4.result())
    result5.append(test5.result())
    result6.append(test6.result())
    result7.append(test7.result())
    result8.append(test8.result())
    result9.append(test9.result())
    result10.append(test10.result())
    result11.append(test11.result())
    result12.append(test12.result())

    time.sleep(2)
    df = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9 + result10 + result11 + result12
    dfFinal = pd.concat(df, ignore_index=True)

    final_results = Performance()
    final_performance = final_results.performance(dfFinal)
    dfFinal.to_clipboard()
    print(dfFinal)
    print(final_performance)

    plt.figure(figsize=(10,6))

    plot1, = plt.plot(dfFinal['NetPnl'])
    plot2, = plt.plot(dfFinal['RlzdDrawdown'])
    plot3, = plt.plot(dfFinal['NewEquityHigh'])

    plt.legend([plot1,plot2,plot3],['NetPnl', 'RlzdDrawdown', 'NewEquityHigh'], fontsize='x-small')
    plt.grid()
    plt.show()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} second(s)')

if __name__ == '__main__':
    print('starting main()')
    main()


