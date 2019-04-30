import pandas as pd
import numpy as np
import re



df=pd.read_csv("C:/Users/Ananda/Downloads/train.csv") ####path of the data
####to handle empty rows
df.dropna(how="all", inplace=True)
##to remove duplicate records in the data
df = df.drop_duplicates()
###to remove punctuations and other special characters from the column names 
cols=list(df.columns)
a=[]
for cl in cols:
    cl=re.sub('[^A-Za-z0-9_.]+',"",cl)
    a.append(cl)
df.columns=a
###to remove punctuations and special characters from the dataset
cols=list(df.columns)
for i in cols:
    try:
        df[i]=df[i].apply(lambda x: re.sub('[^0-9A-Za-z-/]+',"",x))
        ##to handle non ASCII characters
        df[i]=df[i].apply(lambda x: re.sub(r'[^\x00-\x7F]+',' ', x))
    except:
        None

##to handle outliers
def outlier_treatment(df,kk):
    q1=df[kk].quantile(0.25)
    q3=df[kk].quantile(0.75)
    iqr=q3-q1
    quantiles=[q1-1.5*iqr,q3+1.5*iqr]
    return quantiles

numeric_data=df.select_dtypes([np.number]).columns 
for kk in numeric_data:
    outlier_ip=outlier_treatment(df,kk)
    df.loc[df[kk]<outlier_ip[0],kk]=outlier_ip[0]
    df.loc[df[kk]>outlier_ip[1],kk]=outlier_ip[1]

####imputation
for kk in numeric_data:
    try:
        if df[kk].isnull().sum()/len(df[kk]) < 0.1:
            kk_mean=df[kk].mean()
            df[kk] =df[kk].apply(lambda x: np.where(pd.isnull(x),kk_mean,x))
    except:
        None

number_of_variabbles=len(df.columns)
    

