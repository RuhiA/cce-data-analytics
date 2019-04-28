# cce-data-analytics
This repo is for the project assignment of Data Analytics 2019 Jan-May batch.


# statistics and linear regression Module
[lr_utils.py ](lr_utils.py)
It is an utility to for estimating the value using linear regression model. It works for multivariate data.

This can be run using the following commnad

```
LinearRegression().solve_and_estimate("<csv data file>","<target column>","<x1= value1>","<x2= value2>",...,"<x3= value3>")
```
Sample :
```
LinearRegression().solve_and_estimate("data/multivariate-date.csv","Salary","Education=16","Experience=5","Hours per week=50")
```
this command will produce the estimated value of Salary when Education = 16, experience =5 and hours per week =50  

Test file. : 
[Test file ](test/linear-regrestion-test.py)

Functions provided in this utility

| function     | solve_regression |
|--------------|------------|
| Description  | This function fits the regression model on the given data |
| template     | solve_and_estimate("<csv data file>","<target column>","x1","x2",...,"x3") |
| return value | LinearRegressionResponse [lr_functions.py ](lr_functions.py) |
| Example      | LinearRegression().solve_regression("data/multivariate-date.csv","Salary","Education","Experience","Hours per week") |

| function     | estimate_value |
|--------------|-------------   |
| Description  | This function is to estimate the value given the equation parameters  of regression model|
| template     | estimate_value(<linera_equation_params,x1_value,x2_value,s3_value,...) |
| return value | decimal value |
| Example      | LinearRegression().estimate_value(response.equation_params,16,5,50) |

| function     | solve_and_estimate |
|--------------|-------------   |
| Description  | This function is to solve the regression and  estimate the value given the equation parameters  of regression model|
| template     | solve_and_estimate("<csv data file>","<target column>","<x1= value1>","<x2= value2>",...,"<x3= value3>") |
| return value | None(It prints on console) |
| Example      | LinearRegression().solve_and_estimate("data/multivariate-date.csv","Salary","Education=16","Experience=5","Hours per week=50")
 |

| Info | Details |
|--------------|------------|
| function     | round_float |
| Description  | To calculate the round of decimal value uo to 2 decimal places |
| template     | round_float(floatValue) |
| return value | decimal value upto two decimal places |
| Example      | round_float(10.96996) |

| Info | Details |
|--------------|------------|
| function     | sum_of_columns |
| Description  | To calculate the sum of  column values in given Data set |
| template     | sum_of_columns(dataSet, columnName) |
| return value | decimal value |
| Example      | sum_of_columns( dataSet, "Salary")|

| Info | Details |
|--------------|------------|
| function     | mean_of_column |
| Description  | To calcuate the mean of the column |
| template     | mean_of_column( dataSet, columnName) |
| return value | decimal value|
| Example      | mean_of_column( dataSet,  "Salary") |

| Info | Details |
|--------------|------------|
| function     | sum_of_x_minus_x_bar |
| Description  | To calculated the sum of all the values from its mean( Sum(x-xbar) ) |
| template     | sum_of_x_minus_x_bar( dataSet, columnName) |
| return value | decimal value |
| Example      | sum_of_x_minus_x_bar( dataSet,  "Salary") |

| Info | Details |
|--------------|------------|
| function     | sum_of_squares |
| Description  | To calculated the sum of squares of a given column |
| template     | sum_of_squares( dataSet, columnName) |
| return value | decimal value |
| Example      | sum_of_squares( dataSet,  "Salary") |

| Info | Details |
|--------------|------------|
| function     | sum_of_muliplication_of_cols |
| Description  | sum_of_muliplication_of_cols( dataSet, columnName1, columnName2)|
| template     | round_float(floatValue) |
| return value | decimal value |
| Example      | sum_of_muliplication_of_cols( dataSet,  "x-xbar",  "y-ybar") |

| Info | Details |
|--------------|------------|
| function     | standard_deviation |
| Description  | To calculate the standard deviation of the given columns|
| template     | standard_deviation(dataSet, columnName) |
| return value | decimal value |
| Example      | standard_deviation(dataSet,  "Salary") |

| Info | Details |
|--------------|------------|
| function     | covariance |
| Description  | To calculate the covariance of the two columns |
| template     | covariance(dataSet, featureColumn, actualValueColumn) |
| return value | decimal value |
| Example      | covariance(dataSet, "x", "y")  |

| Info | Details |
|--------------|------------|
| function     | find_corr_coeff |
| Description  | To calcuate the correlation coefficient of two columns |
| template     | find_corr_coeff(dataSet, featureColumn, actualValueColumn) |
| return value | Object CorrelationCoeff with value corr and isSignificant |
| Example      | find_corr_coeff(dataSet, featureColumn, actualValueColumn) |

| Info | Details |
|--------------|------------|
| function     | check_correlation_coeff |
| Description  | To calcuate the correlation coefficient of  target column with each of the independent variable (feature) columns |
| template     | check_correlation_coeff(inputFile , valueColumn, *featureColumns ) |
| return value | prints the correlation coefficient on console and wether it is significant |
| Example      | check_correlation_coeff(inputFile , "y", "x1,"x2",..,"xn" ) |

| Info | Details |
|--------------|------------|
| function     | find_parameters_for_multivariate |
| Description  | To calculate the estimated parameter values for linear regression model |
| template     | find_parameters_for_multivariate(inputFile, actualValueColumn, *featureColumn )|
| return value | all the parameter values in form of array |
| Example      | find_parameters_for_multivariate(inputFile, "y", "x1,"x2",..,"xn") |

| Info | Details |
|--------------|------------|
| function     | estimate_value |
| Description  | This gives the estimated value of the target columngiven all the independent variables  using the linear regression model |
| template     | estimate_value(params, *featureValue)  |
| return value | decimal value |
| Example      | estimate_value(params, "50,"6",,,"10")  |

| Info | Details |
|--------------|------------|
| function     | build_anova_table |
| Description  | This builds the avova table for linear regresission model |
| template     | build_anova_table(inputFile, params, targetColumn, *featureNames) |
| return value | prints anova table on console |
| Example      | build_anova_table(inputFile, <parameter value found by find_parameters_for_multivariate method> ,"y", "x1,"x2",..,"xn") |

| Info | Details |
|--------------|------------|
| function     | main |
| Description  | This is the main funtion to build and run the linear regression model. As of now it prints output on console. It needs to be changes to retrun all the values so that it can be displayed on UI |
| template     | main(inputFile, targetColumn, *featuresAndValue) |
| return value | prints the end to end result on console |
| Example      | main("<csv data file>","<target column>","<x1= value1>","<x2= value2>",...,"<x3= value3>") <br> main("data/multivariate-date.csv","Salary","Education=16","Experience=5","Hours per week=50")
|

