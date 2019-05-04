import csv
import os
import matplotlib.pyplot as plt
from PACF import *

def csv_reader_for_univariate(input_file):
	first_column = []
	with open (input_file) as csv_file:
	    csv_reader = csv.DictReader(csv_file)
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            line_count += 1
	        first_column.append(float(row["Y"]))
	        line_count += 1
	return first_column

def get_pacf_integration_csv(input_file, number_of_lags):
	Y_axis_time_series_data = csv_reader_for_univariate(input_file)
	rows = get_rows_to_write_to_pacf_file(Y_axis_time_series_data, number_of_lags)
	write_rows_to_pacf_file(rows)
	Y_axis_PACF = call_linear_regression(number_of_lags)
	X_axis_lag = []
	for i in range(1, number_of_lags + 1):
		X_axis_lag.append(i)
	points = []
	for lag in range(1, number_of_lags + 1):
		points.append((X_axis_lag[lag-1], Y_axis_PACF[lag-1]))
	plt.xlim(0, number_of_lags)
	for pt in points:
		plt.plot( [pt[0],pt[0]], [0,pt[1]])
	plt.axhline(y=0, color='k')
	plt.show()
	

def get_pacf_integration_csv_test():
	package_dir = os.path.dirname(os.path.abspath(__file__))
	thefile = os.path.join(package_dir,'data/univariate.csv')
	get_pacf_integration_csv(thefile, 5)

get_pacf_integration_csv_test()
