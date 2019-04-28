## Following steps needs to be followed by integration team.

#### This class describes how to use Functions Defined in Anova_Functions.py File

from Anova_Functions_Main import *

## There are 2 Main methods in Anova_Function.Py file:
## 1. To calculate F-Statistic Values- Method Name: calculate_f_statistic()
## 2. To Compare Models and Output Best Models- Method Name: compare_and_choose_best_model()

#### CASE 1: IF ONLY ANOVA F-Statistic VALUES ARE REQUIRED

## Step-1: Create the Required Inputs
y_arr = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88]
y_cap_arr = [-48.05, 21.04, 90.13, 159.22, 228.31, 297.4, 366.49, 435.58, 504.67, 573.76]
num_estimated_params = 2
alpha_value = 0.05

# Step-2: Create an Object of Anova Class and call the calculate_f_statistic() method with input values
anova = Anova()
response = anova.calculate_f_statistic(y_arr, y_cap_arr, num_estimated_params, alpha_value)

# To see or access output f-statistic values, just access fields via reponse object as given below
print("SSE: ", response.sse)
print("SSR: ", response.ssr)
print("MSE: ", response.mse)
print("MSR: ", response.msr)
print("F: ", response.f)
print("P: ", response.p)
print("Is Result Significant: ", response.isSignificant)


print("-------------------------------------------------------------------------------------------")


#### CASE 2: TO COMPARE MODELS

## Step-1: Create the Required Inputs as done in previous case as well
y_arr = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88]
alpha_value = 0.05

## Non-Linear Regression Model
model_1 = RegressionModel()
model_1.y_cap_arr = [16.79, 42.59, 79.19, 126.59, 184.79, 253.79, 333.59, 429.19, 525.59, 637.79]
model_1.num_estimated_params = 3

## Linear Regression Model
model_2 = RegressionModel()
model_2.y_cap_arr = [-48.05, 21.04, 90.13, 159.22, 228.31, 297.4, 366.49, 435.58, 504.67, 573.76]
model_2.num_estimated_params = 2


models = []
models.append(model_1)
models.append(model_2)

# Step-2: Create an Object of Anova Class and call the compare and compare_and_choose_best_model() method with input values
anova = Anova()
best_model_arr_index = anova.compare_and_choose_best_model(y_arr, models, alpha_value)
print("best model in given array is model at index: ", best_model_arr_index)