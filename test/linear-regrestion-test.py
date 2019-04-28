# add source to path
import sys
sys.path.insert(0, '../')


from lr_utils import *

if __name__ == "__main__" :
	#Option 1 : when regression is to be performed along with estimation of the value 
	LinearRegression().solve_and_estimate("data/multivariate-date.csv","Salary","Education=16","Experience=5","Hours per week=50")

	#Option 2 : when only regression is to be performed
	response = LinearRegression().solve_regression("data/multivariate-date.csv","Salary","Education","Experience","Hours per week")
	#print("--------------------------Correlation Coefficient ---------------------- ")
	for corr_value in response.r_values:
			print (corr_value.logMessage)

	print(response.equtation_str)
	print("---------------------------Anova stats----------------------------------")
	print(response.anova.sse)
	print(response.anova.ssr)
	print(response.anova.mse)
	print(response.anova.msr)
	print(response.anova.f)
	print(response.anova.p)
	print(response.anova.isSignificant)

	#Option 3 : when value to be estimated when regression is already performed
	print(LinearRegression().estimate_value(response.equation_params,16,5,50))
