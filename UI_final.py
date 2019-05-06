"""
functions to refer for integration or binding the function calls:
1 Data_input :
    Directly calling from "Data_input_functions"  :
    data_input() , Smoothing_file_path() , cleaned_file_path()
2 scatter plot :
     scatter_plot()
3 generate Linear model & anova table:
    generateLinearModel()
4 caluculate y for linear model:
        funtionToFindY()
5 NON Linear model :
        generateNonLinearModel()
6 ACF:
   ACF_call_funtion()
7 PACF:
    PACF_call_function()
8 t-series
    t_series_call_function()
9 ARIMA_MODELLING
    arima_modelling_call_function()

10 SYNTHETIC DATA GENERATION
        synthetic_data_generation_call_func()

"""

import PySimpleGUI as sg
import sys
import pandas as pd
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
from tabulate import tabulate
import pandas as pd
from lr_utils import *
from Data_input_functions import *
Title = "sri venkateshwara Book Store"

PROGRESS_METER_DELAY = 1
class MyGUI():

  
    def SINGLE_LAYOUT(self,cleansed_data_path=None,smoothened_data_path=None,list_of_input_parmeters=None):

        layout=[[sg.Text('Cleansed data CSV file')],
                [sg.InputText('%s'%cleansed_data_path,size=(90,3))],  #1
                [sg.Text('Smoothened data CSV file')],
                [sg.InputText('%s'%smoothened_data_path,size=(90,3))],  #2
                [sg.Text('choose the csv file in drop-down')],
                [sg.InputCombo(('cleansed_csv', 'smoothened_csv'), size=(20, 3))],
                [sg.Text('choose the arguements')],
                [sg.Listbox(values=list_of_input_parmeters, size=(55, 3))],
                [sg.Button("SCATTER_PLOT")],
                [sg.Text('Linear Regression')],
                [sg.Button("GENERATE LINEAR MODEL RETURN ANOVA TABLE")],
                [sg.Listbox(values=('args 1', 'args 2', 'args 3'), size=(35, 3))],  #3
                [sg.InputText('enter arg1')],
                [sg.Text('x1')],
                [sg.InputText('enter arg2')],
                [sg.Text('x2')],
                [sg.InputText('enter arg3')],
                [sg.Text('x3')],
                [sg.Button("CALCUALATE_Y")],
                [sg.Text('NON-Linear Regression')],
                [sg.Button("GENERATE NON-LINEAR MODEL RETURN ANOVA TABLE")],
                [sg.InputText('enter arg1')],  # 3
                [sg.Text('x')],
                [sg.Button("CALCUALATE_Y for parabolic function")],
                [sg.Button("CALCUALATE_Y for exponential function")],
                [sg.Button("ACF",pad=(35,2)),sg.Button("PACF",pad=(35,3)),sg.Button("t-series",pad=(35,4)),
                sg.Button("ARIMA_MODELLING",pad=(5,2)),sg.Button("SYNTHETIC DATA GENERATION",pad=(5,3))]

                ]
        self.window = sg.Window(Title, default_element_size=(40, 1)).Layout(layout)
        self.button, self.values = self.window.Read()
        if self.button == "SCATTER_PLOT":
            self.scatter_plot(self.values)
        elif self.button == "GENERATE LINEAR MODEL RETURN ANOVA TABLE":
            self.generateLinearModel(self.values)
        elif self.button == "CALCUALATE_Y":
            self.funtionToFindY(self.values)
        elif self.button == "CALCUALATE_Y for parabolic function":
            self.funtionToFindY_parabloic(self.values)
        elif self.button == "CALCUALATE_Y for exponential function":
            self.funtionToFindY_exponential(self.values)
        elif self.button == "GENERATE NON-LINEAR MODEL RETURN ANOVA TABLE":
            self.generateNonLinearModel(cleansed_data_path, smoothened_data_path)
        elif self.button == "ACF":
            self.ACF_call_function()
        elif self.button == "PACF":
            self.PACF_call_function()
        elif self.button == "t-series":
            self.t_series_call_function()
        elif self.button == "ARIMA_MODELLING":
            self.arima_modelling_call_function()
        elif self.button == "SYNTHETIC DATA GENERATION":
            self.Synthetic_Data_Generation_call_func()

        print("%s"%self.button)
        print(self.values)
        #sg.Popup(button, values)
        return self.values
    def Synthetic_Data_Generation_call_func(self):
        """

        :return:
        """
        sg.Popup("please integrate synthectic data genereation function")
    def arima_modelling_call_function(self):
        """

        :return:
        """
        sg.Popup("please integrate arima modelling function")

    def t_series_call_function(self):
        """

        :return:
        """
        sg.Popup("please integrate t-series function")

    def ACF_call_function(self):
        """

        :return:
        """
        sg.Popup("please integrate ACF function")

    def PACF_call_function(self):
        """

        :return:
        """
        sg.Popup("please integrate PACF function")


    def funtionToFindY(self,values):
        """
        :return: 
        """
        CSV_to__data=values[2]

        if CSV_to__data =="cleansed_csv":
            file_path = cleansed_file_path
        elif CSV_to__data == "smoothened_csv":
            file_path = smoothened_file_path
            if smoothened_file_path == None:
                sg.Popup("smootehning is not done , please select cleansed csv option")
                return
       
        dataSet = pd.read_csv(file_path)
        y_column = dataSet.columns[0]
        y = 0
        if values[4] == []:
            sg.Popup("please select the number of args")
            return

        elif values[4][0] == 'args 1':
            # y=mx1+c
            if (values[5].count("enter arg") == 1):
                sg.Popup("please enter the value , retry...")
                return

            x1 = float(values[5])

            x_columns = list(dataSet.columns[1:2])
            response = LinearRegression().solve_regression(file_path, y_column, *x_columns)
            y = LinearRegression().estimate_value(response.equation_params, x1)


        elif values[4][0] == "args 2":

            # y=m1x1+m2x2+c
            if ((values[4].count("enter arg") == 1) or (values[5].count("enter arg") == 1)):
                sg.Popup("please enter the value , retry...")
                return

            x1 = float(values[5])
            x2 = float(values[6])

            # y=222
            x_columns = list(dataSet.columns[1:3])
            response = LinearRegression().solve_regression(file_path, y_column, *x_columns)

            y = LinearRegression().estimate_value(response.equation_params, x1, x2)

        elif values[4][0] == "args 3":

            # y=m1x1+m2x2+m3x3

            if (values[5].count("enter arg") == 1) or (values[6].count("enter arg") == 1) or (values[7].count("enter arg") == 1):
                sg.Popup("please enter the value , retry...")
                return

            x1 = float(values[5])
            x2 = float(values[6])
            x3 = float(values[7])
            # y=333.33
            x_columns = list(dataSet.columns[1:4])
            response = LinearRegression().solve_regression(file_path, y_column, *x_columns)
            print(response)
            y = LinearRegression().estimate_value(response.equation_params, x1, x2, x3)
        list_of_messages=[]
        for corr_value in response.r_values:
            list_of_messages.append(corr_value.logMessage)

        multicollinearity_messages=[]
        for corr_value in response.multicollienary_r_values:
            multicollinearity_messages.append(corr_value.logMessage)

        partial_corr_messages=[]
        for corr_value in response.pr_values:
            partial_corr_messages.append(corr_value.logMessage)

        sg.Popup("********Below are the correlation coefficients**********",*list_of_messages, "******* Below are the multicollinearity correlation coefficients **********",*multicollinearity_messages,"********Below are the partial correlation coefficients**********",*partial_corr_messages," ===== Final equation =====",\
                 response.equtation_str,"Y value determined for given x values ",str(y))




    def generateLinearModel(self,values):
        """
        :return:
        """

        CSV_FILE_PATH=values[2]
        CSV_to_plot_data_path = ""
        if CSV_FILE_PATH == "cleansed_csv":
            file_path = cleansed_file_path
        elif CSV_FILE_PATH == "smoothened_csv":
            file_path = smoothened_file_path
            if smoothened_file_path == None:
                sg.Popup("smootehning is not done , please select cleansed csv option")
                return


        self.cal_progress_meter("generating linear model")

        ## Added By Ruhi 
       
       
        dataSet = pd.read_csv(file_path)
        y_column = dataSet.columns[0]
        x_columns = list(dataSet.columns[1:])
        response = LinearRegression().solve_regression(file_path,y_column,*x_columns)

        params = response.equation_params
        dfR = response.anova.dfr
        dfE = response.anova.dfe
        dfT = dfR+dfE
        SSR = response.anova.ssr
        SSE = response.anova.sse
        SST = response.anova.ssr + response.anova.sse
        MSR = response.anova.msr
        MSE = response.anova.mse
        F = response.anova.f
        P = response.anova.p
        list_of_result = [["Regression", dfR, (float(SSR)), (float(MSR)),"-","-"]\
                          ,["Error", dfE, float(SSE), float(MSE),float(F),float(P)]\
                          ,["Total",dfT,float(SST),"-","-","-"]\
                          ]

        headers = ["source","df","SS","MS","F","P"]
        End_table = tabulate(list_of_result,headers,tablefmt="fancy_grid",floatfmt="0.2f")
        print("%s"%End_table)
        sg.Table(End_table)

        sg.Popup("ANOVA_TABLE",End_table)

    def Get_y_and_x_data(self,csv_file_path,get_y_and_x_flag):
        """

        :param csv_file_path:
        :param get_y_and_x_flag:
        :return:
        """
        if get_y_and_x_flag==[]:
            print("no arg selected")
            sg.Popup("please select the arg to plot the data")
            return
        df = pd.read_csv(csv_file_path)
        coloumnNames = list(df.columns)
        y=list(df[coloumnNames[0]])
        x=[]
        for i in range(len(list_of_input_parmeters)):

            if get_y_and_x_flag == list_of_input_parmeters[i]:

                x =list(df[coloumnNames[i+1]])
                break
            else:
                continue

        return y,x

    def scatter_plot(self,values,linearDataList=[]):
        """
        """
        print(values)

        CSV_to_plot_data=values[2]
        CSV_to_plot_data_path=""
        if CSV_to_plot_data == "cleansed_csv":
            CSV_to_plot_data_path=cleansed_file_path
        elif  CSV_to_plot_data == "smoothened_csv":
            CSV_to_plot_data_path = smoothened_file_path
            if smoothened_file_path == None:
                sg.Popup("smootehning is not done , please select cleansed csv option")
                return

        sg.Popup("chosen csv file:%s"%CSV_to_plot_data)
        if values[3] == []:
            sg.Popup("Select the args %s"%list_of_input_parmeters)
            return
        get_y_and_x_flag=values[3][0]
        y=[]
        x=[]
        y,x = self.Get_y_and_x_data(CSV_to_plot_data_path,get_y_and_x_flag)
        print(y)
        print(x)
        if len(y)!=len(x):
            sg.Popup("y and x axis data is not aligned , please check with data input team")
            return
        print("send the csv plot and get the values")
        fig = plt.figure(get_y_and_x_flag+"_"+CSV_to_plot_data)
        ax = fig.add_subplot(1,1,1)
        ax.set_title(get_y_and_x_flag)
        ax.set_ylabel(get_y_and_x_flag.split("->")[0])
        ax.set_xlabel(get_y_and_x_flag.split("->")[1])
        ax.scatter(x,y)
        if linearDataList!=[]:

            ax.plot(linearDataList)

        fig.show()

        #ax.scatter(y,x)



    def cal_progress_meter(self,progress_meter_bar="processing"):


        # Display a progress meter. Allow user to break out of loop using cancel button
        for i in range(PROGRESS_METER_DELAY):
            if not sg.OneLineProgressMeter(progress_meter_bar, i + 1, PROGRESS_METER_DELAY, '.....'):
                break


    def INPUT_CSV(self):

        layout=[[sg.Text('Choose A file', size=(35, 1))],
        [sg.Text('Your file', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('please browse through ->'), sg.FileBrowse()],
         [sg.Submit(), sg.Cancel()]
        ]

        self.InputWindow = sg.Window(Title, default_element_size=(40, 1)).Layout(layout)
        button, values = self.InputWindow.Read()
        if button == "Cancel":
            sys.exit()

        #sg.Popup("raw csv file path", values)
        return values
    def funtionToFindY_parabloic(self,values):
        """
        :return:
        """
        print("determine y")
        print(values)
        y=0
        #y=m1*x*x+m2*x+c
        y=1528.1528
        sg.Popup("DUMMY value IGNORE Y VALUE DETERMINED is :%s"%str(y))

    def funtionToFindY_exponential(self, values):
        print("determine y")
        print(values)
        y = 0
        # y=m1*x*x+m2*x+c
        y = 2610.2610
        sg.Popup("DUMMY VALUE IGNORE Y VALUE DETERMINED is :%s" % str(y))
    def generateNonLinearModel(self,cleansed_data_path,smoothened_data_path):
        """
        :return:
        """
        if smoothened_data_path==None:
            print("call the function to generate linear model with the cleansed file")
        else:
            print("call the function to generate linear model with the smoothened data")
        self.cal_progress_meter("generating linear model")
        dfR = 1
        dfE = 8
        dfT = 9
        SSR = 87
        SSE = 170
        SST = 4487
        MSR = 42
        MSE = 42507
        MST = 4230
        F = 191.3
        P = 0.003
        list_of_result = [["Regression", dfR, (float(SSR)), (float(MSR)),"-","-"]\
                          ,["Error", dfE, float(SSE), float(MSE),float(F),float(P)]\
                          ,["Total",dfT,float(SST),float(MST),"-","-"]\
                          ]

        headers = ["source","df","SS","MS","F","P"]
        End_table = tabulate(list_of_result,headers,tablefmt="fancy_grid",floatfmt="0.2f")
        print("%s"%End_table)
        sg.Table(End_table)

        sg.Popup("please integrate")



# Run the program
if __name__ == "__main__":

    sg.ChangeLookAndFeel('GreenTan')
    obj_GUI = MyGUI()
    obj_data_input=data_input()

    #1.Getting raw csv path
    raw_csv_path = obj_GUI.INPUT_CSV()[0]
    print(raw_csv_path)
    
    #2.processing the raw csv path
    obj_GUI.cal_progress_meter("processing_raw_input_csv_file")
    cleansed_file_path = obj_data_input.cleaned_file_path(raw_csv_path)
    obj_GUI.InputWindow.Close()

    #reading the csv path to get the headers of the csv
    df = pd.read_csv(cleansed_file_path)
    coloumnNames=list(df.columns)
    #form the list of Input parameters to appear in gui
    list_of_input_parmeters=[]
    for i in range(1,len(coloumnNames)):
        list_of_input_parmeters.append((coloumnNames[0]+"->"+coloumnNames[i]))
    print(list_of_input_parmeters)

    
    # 3.option to smoothen data
    values = sg.Popup("Do you want smoothen data", button_type=sg.POPUP_BUTTONS_YES_NO)
    print(values)
    smoothened_file_path=None
    if values == "Yes":
        raw_csv_path = obj_GUI.INPUT_CSV()[0]

        obj_GUI.cal_progress_meter("processing raw smoothened file")
        smoothened_file_path = obj_data_input.Smoothing_file_path(raw_csv_path)
        obj_GUI.InputWindow.Close()

    #main window for computation
    obj_GUI.SINGLE_LAYOUT(cleansed_file_path,smoothened_file_path,list_of_input_parmeters)
    values = sg.Popup("Do you want to retry (or) do more Computation (or) continue", button_type=sg.POPUP_BUTTONS_YES_NO)
    while values == 'Yes':
        obj_GUI.window.Close()
        obj_GUI.SINGLE_LAYOUT(cleansed_file_path,smoothened_file_path,list_of_input_parmeters)
        values = sg.Popup("Do you want to retry (or) do more Computation (or) continue", button_type=sg.POPUP_BUTTONS_YES_NO)

    print("END")