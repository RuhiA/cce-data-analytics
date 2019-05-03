import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import operator
import math
import csv
import collections
import sys
from anova.Anova_Functions_Main import *

class LinearRegressionResponse:
	equtation_str : None
	equation_params : None
	r_values : []
	multicollienary_r_values : []
	anova : AnovaResponse()
	
class CorrelationCoeff :
	param1 : None
	param2: None
	corr_value : None
	isSignificant : None
	logMessage : None

def round_float(floatValue) :
	return round(floatValue, 2)
def sum_of_columns( dataSet, columnName) :
	return sum(dataSet[columnName])

def mean_of_column( dataSet, columnName) :
	print(columnName)
	return round_float(sum(dataSet[columnName])/len(dataSet))

def sum_of_x_minus_x_bar( dataSet, columnName) :
	mean = round_float(mean_of_column(dataSet, columnName))
	tempCol = dataSet[columnName]- mean
	return round_float(sum(tempCol))

def sum_of_squares( dataSet, columnName) :
	return round_float(sum(dataSet[columnName]**2))

def sum_of_muliplication_of_cols( dataSet, columnName1, columnName2) :
	return round_float(sum(dataSet[columnName1]*dataSet[columnName2]))

def standard_deviation(dataSet, columnName) :
	return round_float(math.sqrt(sum((dataSet[columnName]- mean_of_column(dataSet, columnName))**2)/(len(dataSet)-1)))

def variance(dataSet, featureColumn) :
	x_min_xbar = dataSet[featureColumn]- mean_of_column(dataSet, featureColumn)
	v_numerator = x_min_xbar * x_min_xbar
	variance_val = sum(v_numerator)/(len(dataSet)-1)
	return round_float(variance_val)


def covariance(dataSet, featureColumn, actualValueColumn) :
	x_min_xbar = dataSet[featureColumn]- mean_of_column(dataSet, featureColumn)
	y_min_ybar = dataSet[actualValueColumn]- mean_of_column(dataSet, actualValueColumn)
	cov_numerator = x_min_xbar * y_min_ybar
	cor_num = sum(cov_numerator)/(len(dataSet)-1)
	return round_float(cor_num)

def find_corr_coeff(dataSet, featureColumn, actualValueColumn) :
	cor_num = covariance(dataSet, featureColumn, actualValueColumn)
	standard_deviationOfFeatureColumn = standard_deviation(dataSet, featureColumn)
	standard_deviationOfValueColumn = standard_deviation(dataSet, actualValueColumn)
	cor_r = round_float((cor_num)/(standard_deviationOfFeatureColumn*standard_deviationOfValueColumn))
	corr = CorrelationCoeff()
	corr.param1 = featureColumn
	corr.param2 = actualValueColumn
	corr.corr_value = cor_r
	corr.isSignificant = (abs(cor_r) > (1.96/math.sqrt(len(dataSet)))) 
	significant_stmt = "It is significant" if corr.isSignificant else "It is not significant"
	corr.logMessage = "Correlation Coefficient of column '%s' with column '%s' is %s. %s." % (featureColumn, actualValueColumn, cor_r, significant_stmt)
	return corr

def check_correlation_coeff(data , valueColumn, *featureColumns ) :
	corr_coeff_arr = []
	# find correlation coefficient
	for feature in featureColumns:
		corr_value = find_corr_coeff(data, feature, valueColumn)
		corr_coeff_arr.append(corr_value)
	return corr_coeff_arr		

def check_multicollinearity(data, *featureColumns ) :
	corr_coeff_arr = []
	# find multicollinearity
	for i in range(len(featureColumns)):
		for j in range(len(featureColumns)):
			if(j < i) :
				corr_value = find_corr_coeff(data, featureColumns[i], featureColumns[j])
				corr_coeff_arr.append(corr_value)
	return corr_coeff_arr	

def find_parameters_for_multivariate(dataset, actualValueColumn, *featureColumn ) :
	features = list(featureColumn)
	features.append("c")
	data = dataset
	data["c"] = 1

	matrix = []
	i =0
	y_matrix = []
	while i < len(features) :
		row1 = []
		j=0
		while j < len(features) :
			row1.append(sum_of_muliplication_of_cols(data, features[i], features[j]))
			j+=1
		y_matrix.append(sum_of_muliplication_of_cols(data, features[i],actualValueColumn))
		matrix.append(row1)
		i+=1
	A = np.array(matrix)
	print("------------------------------------------------------------------------")
	print("Matrix for solving equations")
	print("A = \n", A)
	B = np.array(y_matrix) 
	print("B =", B)
	print("------------------------------------------------------------------------")
	params = np.linalg.solve(A, B)
	roundedParams = np.asarray([round_float(param) for param in params])
	#build_anova_table(inputFile, params,actualValueColumn, *featureColumn)
	return roundedParams


def estimate_value(params, *featureValue) :
	parameters = params[:-1]
	output = (parameters.dot(featureValue)) + params[-1]
	return output

def calcualate_y_cap(dataSet, params, targetColumn, *featureNames) :
	features = list(featureNames)
	features.append("c")
	dataSet["estimate_value"] = params[len(params)-1]
	i = 0
	while i < len(featureNames) :
		dataSet["estimate_value"] = dataSet["estimate_value"] + params[i] * dataSet[featureNames[i]]
		i = i+1
	return 	dataSet["estimate_value"]

def build_anova_table(inputFile, params, targetColumn, *featureNames) :
	features = list(featureNames)
	features.append("c")
	dataSet = pd.read_csv(inputFile)
	dataSet["estimate_value"] = params[len(params)-1]
	i = 0
	while i < len(featureNames) :
		dataSet["estimate_value"] = dataSet["estimate_value"] + params[i] * dataSet[featureNames[i]]
		i = i+1
	dataSet["squaredError"] = (dataSet["estimate_value"] - dataSet[targetColumn])**2
	dataSet["squaredErrorRegression"] = (dataSet["estimate_value"] - mean_of_column(dataSet,targetColumn))**2
	SSE = sum(dataSet["squaredError"])
	SSR = sum(dataSet["squaredErrorRegression"])
	MSR = SSR / (len(params) -1)
	MSE = SSE / (len(dataSet) -len(params))
	F = MSR/MSE
	anovastats = pd.DataFrame(columns=('source', 'df', 'SS','MS','F'))
	anovastats["source"] = ["regression", "error" ," total"]
	anovastats["df"] = [len(params) -1, (len(dataSet) -len(params)), (len(dataSet) -1)]
	anovastats["SS"] = [SSR, SSE, SSE+SSR]
	anovastats["MS"] = [MSR, MSE, float('nan')]
	anovastats["F"] = [F, float('nan'),float('nan')]
	print("---------------------------Anova stats----------------------------------")
	print(anovastats)
	print("------------------------------------------------------------------------")


def display_linear_equation(params,*features):
	strval =""
	i = 0
	while i < len(params) -1 :
		strval = strval + str(params[i]) + "("+features[i]+")" + (" + " if params[i+1] >= 0 else " ")
		i += 1
	strval  = strval + str(params[i])
	print("Equation : ", strval )
	return strval

def calculate_f_statistic(y_arr, ycap_arr, m, alpha_value):
    # Validating inputs
    dfr = m -1

    if len(y_arr) != len(ycap_arr):
        raise ValueError('Mismatch in the size of y and ^y arrays')

    return Anova().compute_anova(y_arr,ycap_arr, dfr, alpha_value)







