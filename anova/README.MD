There are 2 Python Files in this folder


Anova_Functions_Main.py is the main file which has all the required methods for calculation of f-statistic values and comparision of models. This file needs to be imported by integration team and should be used.


AnovaExecutionSteps.py is the file which list the steps to assist the platform team in integration.
It list all the steps that defines:
a. how to import Anova_Functions_Main file
b. which methods to call for which usecase.
c. the input required by methods
d. response outputs of methods


To Test AnovaExecutionSteps.py can be directly executed as:

py AnovaExecutionSteps.py 


However, Integration team should follow the same steps as done in AnovaExecutionSteps.py in their code to consume Anova_Functions_Main.py file methods.