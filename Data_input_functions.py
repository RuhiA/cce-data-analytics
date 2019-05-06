import pandas as pd
import numpy as np
import re
import os
from UI_final import *

class data_input():
    
    ###data cleaning
    def cleaning(self,df2):
    	df = pd.DataFrame()
    	df=df2.copy()
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
    	        df[i]=df[i].apply(lambda x: re.sub('[^0-9-A-Z-a-z-/]+',"",x))
    	        ##to handle non ASCII characters
    	        df[i]=df[i].apply(lambda x: re.sub(r'[^\x00-\x7F]+',' ', x))
    	        
    	    except:
    	        None
    	return(df)

    ###to return number of variables in dataset
    def count_var(self,new_df):
    	number_of_variables=len(new_df.columns)
    	return number_of_variables
    
    ####to get the outlier limits
    def outlier_limits(self,of,kk):
        q1=of[kk].quantile(0.25)
        q3=of[kk].quantile(0.75)
        iqr=q3-q1
        quantiles=[q1-1.5*iqr,q3+1.5*iqr]
        return quantiles
    
    #########smoothening the data
    def smoothing_list(self,ActValList,a):
        ForcastVallist=[]
        i=0
        for k,x in enumerate(ActValList,start = 0):
          if i == 0:
            ForcastVallist.insert(i,ActValList[0])
            i+=1
          else:
            temp = (a*ActValList[k-1])+((1-a)*ForcastVallist[i-1])
            ForcastVallist.insert(i,round(temp,2))    
            i+=1
        return(ForcastVallist)
    
    def Smoothing(self,df):
        alpha=0.2
        j=0
        cols=list(df.columns)
        new_frame = pd.DataFrame()
        for cl in cols:
            new_list = df[cl].tolist()
            if j == 0 :
                new_frame.insert(j,cl,new_list)
                j+=1
            else:
                Slist =self.smoothing_list(new_list,alpha)
                new_frame.insert(j,cl,Slist)
                j+=1
                print(new_frame)
        new_frame.to_csv('Smoothened_Values_Multi_1.csv',index=False)
        return new_frame
    
    ####to change variable datatypes
    def tryconvert(self,x):
        try:
            float(x)
            return x
        except:
            return None
    
    ####data imputation
    def imputation(self,numeric_data,new_df):
        for kk in numeric_data:
            try:
                if new_df[kk].isnull().sum()/len(new_df[kk]) < 0.1:
                    kk_mean=new_df[kk].mean()
                    new_df[kk] =new_df[kk].apply(lambda x: np.where(pd.isnull(x),kk_mean,x))
            except:
                None
        return(new_df)
    
    ####to change the datatype of variables
    def convdtype(self,cs,new_df):  
        for c in cs:
            new_df[c] = new_df[c].apply(lambda x: np.where(pd.isnull(x),x,self.tryconvert(x)))
            new_df[c] = new_df[c].astype(float)
        return new_df
    
    def cleansing(self,x):
        df3=pd.read_csv(x)
        alpha=0.2
        new_df = pd.DataFrame()
        smooth_df = pd.DataFrame()
        ###Data Cleaning
        df=self.cleaning(df3)
        ###function to return number of variables in a dataset
        n =self.count_var(df)
        print(n)
        ##changing all datatypes to float 
        cs=list(df.columns)
        df=self.convdtype(cs,df)
        ###outlier treatment
        numeric_data=df.select_dtypes([np.number]).columns 
        for kk in numeric_data:
            outlier_ip=self.outlier_limits(df,kk)  ####calling the outlier limits function
            df.loc[df[kk]<outlier_ip[0],kk]=outlier_ip[0]
            df.loc[df[kk]>outlier_ip[1],kk]=outlier_ip[1]
            
        ###to handle imputation
        new_df=self.imputation(numeric_data,df)
        return new_df
    def cleaned_file_path(self,x):       
        cleandata=self.cleansing(x)
        pos1=x.rfind('/')
        pos2=x.rfind('.')
        path1=x[pos1+1:pos2]
        cleandata.to_csv(path1+'_cleaned_data.csv',index=False)
        path=os.path.normpath(os.getcwd()+'\\'+path1+'_cleaned_data.csv')
        return path
    
    def Smoothing_file_path(self,x):
        cleandata=self.cleansing(x)
        smooth_df=self.Smoothing(cleandata)
        pos1=x.rfind('/')
        pos2=x.rfind('.')
        path1=x[pos1+1:pos2]
        smooth_df.to_csv(path1+'_smoothened_data.csv',index=False)
        smoothen_path=os.path.normpath(os.getcwd()+'\\'+path1+'_smoothened_data.csv')
        return smoothen_path
