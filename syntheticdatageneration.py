from lr_functions import *
from lr_utils import *
import pandas as pd
import math
import numpy as np
from acf.py import *

class Synthetic_data_generation:

def
	qtbar=lr_functions.sum_of_columns( dataSet, "2nd")
	qt_1bar=lr_functions.sum_of_columns( dataSet, "1st")
	rt_1=acf.get_auto_correlation(list1,list2,1)
	st=lr_functions.standard_deviation(dataSet,"2nd")
	st_1=lr_functions.standard_deviation(dataSet,"1st")
	Zt=np.random.randn(1)

def calcuate_qt(qtbar,qt_1,qt_1bar,St,St_1,rt_1,Zt)
	bt=rt_1*(St/St_1)
	b=math.sqrt(1-int(math.pow(rt_1,2))
	qt=qtbar+bt(qt_1-qt_1bar)+Zt*St*(b)
	return qt
	