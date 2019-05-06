import csv
import os
import matplotlib.pyplot as plt
from ACF import get_correlogram
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from pandas import Series
from matplotlib import pyplot
import pandas as pd

def csv_reader_for_univariate(input_file, column_name):
	first_column = []
	with open (input_file) as csv_file:
	    csv_reader = csv.DictReader(csv_file)
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            line_count += 1
	        first_column.append(float(row[column_name]))
	        line_count += 1
	return first_column

def get_correlogram_integration_csv(input_file, column_name, number_of_lags):
	Y_axis_time_series_data = csv_reader_for_univariate(input_file,column_name)
	Y_axis_ACF = get_correlogram(Y_axis_time_series_data, number_of_lags)
	X_axis_lag = []
	for i in range(1, number_of_lags + 1):
		X_axis_lag.append(i)
	plt.step(X_axis_lag, Y_axis_ACF)
	plt.show()

	
#get_correlogram_integration_csv('/Users/ruhiagrawal/Downloads/Khanapur_Flows_1981-2001_formated.csv','Discharge', 20)

series =  pd.Series(csv_reader_for_univariate('/Users/ruhiagrawal/Downloads/Khanapur_Flows_1981-2001_formated.csv','Discharge'))
#series.plot()
#pyplot.show()

#plot_acf(series,lags=20)
#pyplot.show()

plot_pacf(series, lags=20)
pyplot.show()