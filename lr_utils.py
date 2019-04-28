import pandas as pd

from lr_functions import *
class LinearRegression :

	def solve_regression(self, inputFile, targetColumn, *features):
		dataSet = pd.read_csv(inputFile)
		response = LinearRegressionResponse()
		r_values = check_correlation_coeff(dataSet,targetColumn, *features)
		params = find_parameters_for_multivariate(dataSet,targetColumn,*features)
		strval = display_linear_equation(params, *features)
		y_arr = dataSet[targetColumn]
		ycap_arr = calcualate_y_cap(dataSet, params, targetColumn, *features)
		anova_response = calculate_f_statistic(y_arr, ycap_arr, len(params), 0.05)
		response.r_values = r_values
		response.equtation_str = strval
		response.equation_params = params
		response.anova = anova_response
		return response

	def estimate_value(self, params, *featureValue) :
		parameters = params[:-1]
		output = (parameters.dot(featureValue)) + params[-1]
		return output

	def solve_and_estimate(self, inputFile, targetColumn, *featuresAndValue):
		features =[elem.split('=', 1)[0] for elem in featuresAndValue]
		values =[float(elem.split('=', 1)[1]) for elem in featuresAndValue]
		response = self.solve_regression(inputFile, targetColumn, *features)

		for corr_value in response.r_values:
				print (corr_value.logMessage)
		print("---------------------------Anova stats----------------------------------")
		print(response.anova.sse)
		print(response.anova.ssr)
		print(response.anova.mse)
		print(response.anova.msr)
		print(response.anova.f)
		print(response.anova.p)
		print(response.anova.isSignificant)

		output = estimate_value(response.equation_params, *values)
		print("Output : ", output )