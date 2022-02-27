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

The walk-forward method is more challenging to code, since there are multiple iterations going on. 


