import sys
import csv
import os

my_package_dir = os.path.dirname(os.path.abspath(__file__))
root_dir, file = os.path.split(my_package_dir)
pacf_multivariate = os.path.join(my_package_dir,'data/acf_multivariate.csv')
sys.path.append(root_dir)
from lr_utils import *

def get_lagged_list(list, lag):
	if lag == 0:
		return list
	else:
		lagged_list = [0] + list
		lagged_list.pop()
		return get_lagged_list(lagged_list, lag - 1)	

def remove_first_x_values(list, number):
	for lag in range(1, number + 1):
		list.pop(0)

def get_rows_to_write_to_pacf_file(Y, number_of_lags):
	lagged_lists = []
	for lag in range(1, number_of_lags + 1):
		lagged_list = get_lagged_list(Y, lag)
		lagged_lists.append(lagged_list)
	for lagged_list in lagged_lists:
		remove_first_x_values(lagged_list, number_of_lags)
	remove_first_x_values(Y, number_of_lags)
	Y_with_header = ['Y'] + Y
	for lag in range(1, number_of_lags + 1):
		lagged_lists[lag-1] = ['Y_lagged_' + str(lag)] + lagged_lists[lag-1]
	rows = zip(Y_with_header, *lagged_lists)
	return rows

def write_rows_to_pacf_file(rows):
	with open(pacf_multivariate, 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerows(rows)

def call_linear_regression(number_of_lags):
	feature_list = []
	for i in range(1, number_of_lags + 1):
		feature = "Y_lagged_" + str(i)
		feature_list.append(feature)
	response = LinearRegression().solve_regression(pacf_multivariate, "Y",*feature_list)
	print(response.equation_params)
	equation_coeffs = response.equation_params.tolist()
	equation_coeffs.pop()
	return equation_coeffs

def get_pacf_test():
	# Y = [1,2,3,4,5,6,7,8,9,10]
	Y = [266,145.9,183.1,119.3,180.3,168.5,231.8,224.5,192.8,122.9,336.5,185.9,194.3,149.5,210.1,273.3,191.4,287,226,303.6,289.9,421.6,264.5,342.3,339.7,440.4,315.9,439.3,401.3,437.4,575.5,407.6,682,475.3,581.3,646.9]
	X_axis_time = []
	for i in range(1, len(Y) + 1):
		X_axis_time.append(i)
	plt.plot(X_axis_time, Y)
	plt.show()

	number_of_lags = 10
	rows = get_rows_to_write_to_pacf_file(Y, number_of_lags)
	write_rows_to_pacf_file(rows)
	Y_axis_PACF = call_linear_regression(number_of_lags)
	print(Y_axis_PACF)
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
	threshold = 1.96 / len(Y_axis_time_series_data)
	plt.axhline(y=threshold, color='k', linestyle='dashed')
	plt.axhline(y=-threshold, color='k', linestyle='dashed')
	plt.show()

# get_pacf_test()

