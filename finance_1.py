import datetime as dtime
import matplotlib.pyplot as pplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0)
