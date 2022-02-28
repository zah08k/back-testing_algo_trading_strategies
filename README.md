# back-testing_algo_trading_strategies
I've created an environment where I can develop and back-test various algorithmic trading strategies with the method of walk-forward optimization

There are libraries in Python that can be used to back-test trading strategies. However, I wanted to create my own environment - for practice purposes, but also with the idea, that I can customize the strategies and the back-testing process.

The core idea is to be able to back-test with the method of walk-forward optimiziation. The most popular way of backtesting is dividing the sample data into 80% in-sample and 20% out-of-sample data. However, with the walk-forward method, we get more out-of-sample results. For example if we have data from 2006 until 2022, we can train, optimize and test our strategy the following way:

2006 - 2010 -> train and optimize (5 years in-sample data)
2011        -> test (1 year out-of-sample data)

2007 - 2011 -> train and optimize (5 years in-sample data)
2012        -> test (1 year out-of-sample data)

2008 - 2012 -> train and optimize (5 years in-sample data)
2013        -> test (1 year out-of-sample data)

etc.

Considering the example above, at the end we would have 11-12 years out-of-sample results. With the 80/20 method, however, we would only have around 3-4 years out-of-sample results.

The walk-forward method is more challenging to code, since there are multiple iterations going on. In my code I can choose to optimize 1 parameter and find the best filters.

backtest -> this is the walk-forward optimization code, but also the performance code, where we get the final results (PnL, Winrate, Max drawdown, max consecutive losses etc.)

calendars -> from here we can use various strategies based for example on opening long or short positions only on specific days.

candlesticks -> various candlestick formations and patterns

filters - > various filters, based on momentum, trend, volatility etc.

indicators - > various indicators, based again on momentum, trend, volatility etc.

With the files above we can start back-testing and experimenting with different strategies. For example if I want to back-test a specific indicator, I simply call the indicator from the class in the file named 'indicators'.

I've put 2 examples of trading strategies with nice looking equity curve, one based on momentum (_101-cl-bb-momentum.py - Crude Oil) and the other based on mean-reversion (_101-zc-highestlowest-meanreversion.py - Corn).  

To make the code faster, since there are multiple iterations, I also use multiprocessing.


