import PySimpleGUI as sg
import sys
import pandas as pd
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
from tabulate import tabulate
from lr_utils import *
Title = "sri venkateshwara Book Store"

PROGRESS_METER_DELAY = 5
class MyGUI():

  
    def SINGLE_LAYOUT(self,cleansed_data_path=None,smoothened_data_path=None):

        layout=[[sg.Text('Cleansed data CSV file')],
                [sg.InputText('%s'%cleansed_data_path)],  #1
                [sg.Text('Smoothened data CSV file')],
                [sg.InputText('%s'%smoothened_data_path)],  #2
                [sg.InputCombo(('cleansed_csv', 'smoothened_csv'), size=(20, 3))],
                [sg.Listbox(values=('y->x1', 'y->x2', 'y->x3'), size=(55, 3))],
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
                [sg.Button("CALCUALATE_Y for exponential function")]



                ]
        self.window = sg.Window(Title, default_element_size=(40, 1)).Layout(layout)
        self.button, self.values = self.window.Read()
        if self.button == "SCATTER_PLOT":
           # self.scatter_plot('XValues','YValues','The Scatter plot',[0,1,2],[3,4,5])
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


        print("%s"%self.button)
        print(self.values)
        #sg.Popup(button, values)
        return self.values

    def CALL_CLEANSING_FUNC(self,raw_csv_path):
        """
        :param raw_csv_path:
        :return:cleansed_file_csv_path
        """
        cleansed_file_path= raw_csv_path #"c:\cleansedData.csv"
        sg.Popup("****cleansed data in the path :%s *******"%cleansed_file_path)
        return cleansed_file_path
    def CALL_SMOOTHENING_FUNC(self,raw_csv_path):
        """
        :param raw_csv_path:
        :return:smoothened_file_csv_path
        """
        smoothened_file_path="c:\smoothened_data.csv"
        sg.Popup("****smoothened data in the path :%s *******"%smoothened_file_path)
        return smoothened_file_path
    def funtionToFindY(self,values):
        """
        :return:
        """
        print("determine y")
        print(values)
        y=0
        if values[4] == []:
            sg.Popup("please select the number of args")
            return

        elif values[4][0] == 'args 1':
            #y=mx1+c
            if (values[5].count("enter arg") == 1) :
                sg.Popup("please enter the value , retry...")
                return

            x1 = values[5]
            y=111#for now hardcoded

        elif values[4][0] == "args 2":

            #y=m1x1+m2x2+c
            if  ((values[4].count("enter arg") == 1) or (values[5].count("enter arg") == 1)):
                sg.Popup("please enter the value , retry...")
                return

            x1 = values[5]
            x2 = values[6]

            y=222
        elif values[4][0] == "args 3":

            #y=m1x1+m2x2+m3x3

            if (values[5].count("enter arg") == 1) or (values[6].count("enter arg") == 1) or (values[7].count("enter arg") == 1):
                sg.Popup("please enter the value , retry...")
                return

            x1 = values[5]
            x2 = values[6]
            x3 = values[7]
            y=333.33
        sg.Popup("Y VALUE DETERMINED is :%s"%str(y))


    def generateLinearModel(self,values):
        """
        :return:
        """
        #Note:we are not giving the option to choose to generate a linear regression model for
        # cleansed & smoothened file
        #if user clicks on the smoothened data , we are passing the smoothened data
        #else
        # we are passing the jus cleansed file

        # if smoothened_data_path==None:
        #     print("call the function to generate linear model with the cleansed file")
        # else:
        #     print("call the function to generate linear model with the smoothened data")
        CSV_FILE_PATH=values[2]


        self.cal_progress_meter("generating linear model")

        ## Added By Ruhi 
        file_path = "test/data/multivariate_4-date.csv"
        dataSet = pd.read_csv(file_path)
        y_column = dataSet.columns[0]
        x_columns = list(dataSet.columns[1:])
        response = LinearRegression().solve_regression(file_path,y_column,*x_columns)
        estimated_output = LinearRegression().estimate_value(response.equation_params,16,5,50,50,50)
       # if values[3]==[]:
       #     sg.Popup("Select the args (y-> x1 or x2 or x3)")
       #     return
       # self.scatter_plot(values,linearDataList=[2.5,3.1,4.6,5.3,6.2,7.8,8.3,9.1,10.2,9.4])

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
        #get the data from the data input team
        if get_y_and_x_flag=="y->x1":
            #get y and x1 data in list form
            y=[1,2,3,4,5,6,7,8,9,10]
            x =[3,5,1,7,2,6,4,7,1,4]
        elif get_y_and_x_flag=="y->x2":
            #get y and x2 data in list form
            y=[1,2,3,4,5,6,7,8,9,10]
            x =[3,5,1,7,2,6,4,7,1,4]
        elif get_y_and_x_flag == "y->x3":
            # get y and x3 data in list form
            y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            x = [3, 5, 1, 7, 2, 6, 4, 7, 1, 4]
        else:
            print("no arg selected")
            sg.Popup("please select the arg to plot the data")
        return y,x
    def scatter_plot(self,values,linearDataList=[]):
        """
        """
        print(values)

        CSV_to_plot_data=values[2]
        sg.Popup("chosen csv file:%s"%CSV_to_plot_data)
        if values[3] == []:
            sg.Popup("Select the args (y-> x1 or x2 or x3)")
            return
        get_y_and_x_flag=values[3][0]
        y=[]
        x=[]
        y,x = self.Get_y_and_x_data(CSV_to_plot_data,get_y_and_x_flag)
        print(y)
        print(x)
        print("send the csv plot and get the values")
        fig = plt.figure(get_y_and_x_flag)
        ax = fig.add_subplot(1,1,1)
        ax.set_title(get_y_and_x_flag)
        ax.set_ylabel(get_y_and_x_flag.split("->")[0])
        ax.set_xlabel(get_y_and_x_flag.split("->")[1])
        ax.scatter(x,y)
        if linearDataList!=[]:

            ax.plot(linearDataList)

        fig.show()

        #ax.scatter(y,x)


    '''
    def scatter_plot(self,XLabel,YLabel,plotLabel,XValues,YValues):
        """
        :return:
        """
        plt.title("y->x1")
        plt.xlabel(XLabel, fontsize=16)
        plt.ylabel(YLabel, fontsize=16)
        plt.suptitle(plotLabel, fontsize=20)
        plt.scatter(XValues , YValues)
        linear_data=[float(1.5),float(2.3),4]
        plt.plot(XValues , linear_data)
       # plt.plot(XValues, YValues)
       # sg.Popup("The Plot displayed")

        plt.show(block=False)
        #plt .close()
        print("debug line")
        self.window.Close()
        return

'''
    def cal_progress_meter(self,progress_meter_bar="processing"):


        # Display a progress meter. Allow user to break out of loop using cancel button
        for i in range(PROGRESS_METER_DELAY):
            if not sg.OneLineProgressMeter(progress_meter_bar, i + 1, PROGRESS_METER_DELAY, '.....'):
                break


    def INPUT_CSV(self):

        layout=[[sg.Text('Choose A file', size=(35, 1))],
        [sg.Text('Your file', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default File path'), sg.FileBrowse()],
         [sg.Submit(), sg.Cancel()]
        ]



        self.InputWindow = sg.Window(Title, default_element_size=(40, 1)).Layout(layout)
        button, values = self.InputWindow.Read()
        if button == "Cancel":
            sys.exit()

        #sg.Popup("raw csv file path", values)
        return values

    def SMOOTHEN_DATA(self):

        layout=[[sg.Text('smoothen data', size=(35, 1))],
        [sg.Text('Your file', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default File path'), sg.FileBrowse()],
         [sg.Ok(), sg.Cancel()]
        ]



        self.smoothenedWindow = sg.Window(Title, default_element_size=(40, 1)).Layout(layout)
        button, values = self.smoothenedWindow.Read()
        #sg.Popup(button, values)
    def funtionToFindY_parabloic(self,values):
        """
        :return:
        """
        print("determine y")
        print(values)
        y=0
        #y=m1*x*x+m2*x+c
        y=1528.1528
        sg.Popup("Y VALUE DETERMINED is :%s"%str(y))

    def funtionToFindY_exponential(self, values):
        print("determine y")
        print(values)
        y = 0
        # y=m1*x*x+m2*x+c
        y = 2610.2610
        sg.Popup("Y VALUE DETERMINED is :%s" % str(y))
    def generateNonLinearModel(self,cleansed_data_path,smoothened_data_path):
        """
        :return:
        """
        #Note:we are not giving the option to choose to generate a linear regression model for
        # cleansed & smoothened file
        #if user clicks on the smoothened data , we are passing the smoothened data
        #else
        # we are passing the jus cleansed file

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

        sg.Popup(Title,End_table)

# Run the program
if __name__ == "__main__":

    sg.ChangeLookAndFeel('GreenTan')
    obj_GUI = MyGUI()


    raw_csv_path = obj_GUI.INPUT_CSV()

    obj_GUI.cal_progress_meter("processing_raw_input_csv_file")
    cleansed_file_path = obj_GUI.CALL_CLEANSING_FUNC(raw_csv_path)
    obj_GUI.InputWindow.Close()

    values = sg.Popup("Do you want smoothen data", button_type=sg.POPUP_BUTTONS_YES_NO)
    print(values)
    smoothened_file_path=None
    if values == "Yes":
        raw_csv_path = obj_GUI.INPUT_CSV()

        obj_GUI.cal_progress_meter("processing raw smoothened file")
        smoothened_file_path = obj_GUI.CALL_SMOOTHENING_FUNC(raw_csv_path)
        obj_GUI.InputWindow.Close()

    obj_GUI.SINGLE_LAYOUT(cleansed_file_path,smoothened_file_path)
    values = sg.Popup("Do you want to do more Computation or continue", button_type=sg.POPUP_BUTTONS_YES_NO)
    while values == 'Yes':
        obj_GUI.window.Close()
        obj_GUI.SINGLE_LAYOUT(cleansed_file_path,smoothened_file_path)
        values = sg.Popup("Do you want to do more Computation or continue", button_type=sg.POPUP_BUTTONS_YES_NO)

    print("END")