import datetime as dtime
import matplotlib.pyplot as pplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dtime.datetime(2000, 1, 1)
end = dtime.datetime(2017, 4, 20)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.head())