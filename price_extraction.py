import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import sys
print(sys.version)
from pandas_datareader import data, wb
import fix_yahoo_finance as yf
yf.pdr_override()
import numpy as np
import datetime

price_changes = []
avg_change = 0
#To get data:
def extract():

	year = 2019
	month = 3
	day = 6

	start = datetime.datetime(year, month, day)
	end = datetime.datetime(year, month, day)

	tickers = ['VOW3.DE', 'F', 'TM', 'HMC']

	for ticker in tickers:
		print ticker
		d = data.get_data_yahoo(ticker, start, end)
		prices = d.iloc[0]
		price_change = prices[3] - prices[0]
		price_changes.append(price_change)

	avg_change = np.mean(price_changes)