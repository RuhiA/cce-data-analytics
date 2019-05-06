import csv
import os
import matplotlib.pyplot as plt
from Non_linear_regression_quadratic import fit_non_regression_quadratic_equation
from Non_linear_regression_quadratic import get_non_linear_quadratic_estimated_values_of_y
from Non_linear_regression_quadratic import get_non_linear_quadratic_estimated_value_of_y

import sys
package_dir = os.path.dirname(os.path.abspath(__file__))
import_path, file = os.path.split(package_dir)
import_file = os.path.join(import_path,'anova')
sys.path.append(import_file)
from Anova_Functions_Main import Anova

def csv_reader_for_bivariate(input_file):
	first_column = []
	second_column = []
	with open (input_file) as csv_file:
	    csv_reader = csv.DictReader(csv_file)
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            line_count += 1
	        first_column.append(float(row["Y"]))
	        second_column.append(float(row["X"]))
	        line_count += 1
	return first_column, second_column

def fit_non_regression_quadratic_integration_equation(input_file, find_Y_hat_at_X):
	solved_parameters = []
	Y,X = csv_reader_for_bivariate(input_file)
	solved_parameters = fit_non_regression_quadratic_equation(X, Y)
	print("y = m1 x^2 + m2 x + c")
	print('y = {0} x^2 + {1} x + {2}'.format(solved_parameters[0], solved_parameters[1], solved_parameters[2]))
	Y_hat = get_non_linear_quadratic_estimated_values_of_y(solved_parameters, X)
	plt.scatter(X, Y)
	plt.plot(X, Y_hat)
	plt.show()
	print(get_non_linear_quadratic_estimated_value_of_y(solved_parameters, find_Y_hat_at_X))
	degreesOfFreedom = 1
	alpha_value = 0.05
	anovaResult = Anova().compute_anova(Y,Y_hat, degreesOfFreedom, alpha_value)
	print("Anova results")
	print(anovaResult.sse)
	print(anovaResult.ssr)
	print(anovaResult.mse)
	print(anovaResult.msr)
	print(anovaResult.f)
	print(anovaResult.p)

def fit_non_regression_quadratic_integration_equation_test():
	package_dir = os.path.dirname(os.path.abspath(__file__))
	thefile = os.path.join(package_dir,'data/bivariate.csv')
	find_Y_hat_at_X = 5
	fit_non_regression_quadratic_integration_equation(thefile, find_Y_hat_at_X)

fit_non_regression_quadratic_integration_equation_test()