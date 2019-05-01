import PySimpleGUI as sg
import sys
import pandas as pd
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
from tabulate import tabulate
Title = "sri venkateshwara Book Store"
class MyGUI():

    def SINGLE_LAYOUT(self,cleansed_data_path=None,smoothened_data_path=None):

        layout=[[sg.Text('Cleansed data CSV file')],
                [sg.InputText('%s'%cleansed_data_path)],  #1
                [sg.Text('Smoothened data CSV file')],
                [sg.InputText('%s'%smoothened_data_path)],  #2
                [sg.InputCombo(('cleansed_csv', 'smoothened_csv'), size=(20, 3))],
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
            self.scatter_plot('XValues','YValues','The Scatter plot',[0,1,2],[3,4,5])

        elif self.button == "GENERATE LINEAR MODEL RETURN ANOVA TABLE":
            self.generateLinearModel(cleansed_data_path,smoothened_data_path)
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
        cleansed_file_path="c:\cleansedData.csv"
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
        if values[3] == []:
            sg.Popup("please select the number of args")
            return

        elif values[3][0] == 'args 1':
            #y=mx1+c
            if (values[4].count("enter arg") == 1) :
                sg.Popup("please enter the value , retry...")
                return

            x1 = values[4]
            y=111#for now hardcoded

        elif values[3][0] == "args 2":

            #y=m1x1+m2x2+c
            if  ((values[4].count("enter arg") == 1) or (values[5].count("enter arg") == 1)):
                sg.Popup("please enter the value , retry...")
                return

            x1 = values[4]
            x2 = values[5]

            y=222
        elif values[3][0] == "args 3":

            #y=m1x1+m2x2+m3x3

            if (values[4].count("enter arg") == 1) or (values[5].count("enter arg") == 1) or (values[6].count("enter arg") == 1):
                sg.Popup("please enter the value , retry...")
                return

            x1 = values[4]
            x2 = values[5]
            x3 = values[6]
            y=333.33
        sg.Popup("Y VALUE DETERMINED is :%s"%str(y))


    def generateLinearModel(self,cleansed_data_path,smoothened_data_path):
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
        SSR = 425089
        SSE = 17089
        SST = 44879.15
        MSR = 425089
        MSE = 42507
        MST = 4230987
        F = 199.3
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


    def cal_progress_meter(self,progress_meter_bar="processing"):


        # Display a progress meter. Allow user to break out of loop using cancel button
        for i in range(2000):
            if not sg.OneLineProgressMeter(progress_meter_bar, i + 1, 2000, '.....'):
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

    obj_GUI.SINGLE_LAYOUT()
    values = sg.Popup("Do you want to do more Computation", button_type=sg.POPUP_BUTTONS_YES_NO)
    while values == 'Yes':
        obj_GUI.window.Close()
        obj_GUI.SINGLE_LAYOUT()
        values = sg.Popup("Do you want to do more Computation", button_type=sg.POPUP_BUTTONS_YES_NO)

    print("END")