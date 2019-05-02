import pandas as pd
import numpy as np
import re

df2=pd.read_csv("C:/Users/LENOVO1/Downloads/Dataset - Bivariant- Sweden Insurance claim.csv") ####path of the data  ###here we need to call the ui.input function 
new_df = pd.DataFrame()
out_df = pd.DataFrame()
smooth_df = pd.DataFrame()
def cleaning(df2):
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
	        df[i]=df[i].apply(lambda x: re.sub('[^0-9/]+',"",x))
	        ##to handle non ASCII characters
	        df[i]=df[i].apply(lambda x: re.sub(r'[^\x00-\x7F]+',' ', x))
	        
	    except:
	        None
	return(df)

new_df = cleaning(df2)


cs=list(new_df.columns)
for c in cs:
	new_df[c] = new_df[c].astype(float)
###function to return number of variables in a dataset
def count_var(new_df):
	number_of_variables=len(new_df.columns)
	return number_of_variables

n = count_var(new_df)
print(n)

new_df.to_csv('Cleaned_file_Ex25.csv',index=False)

def outlier(of):
	##to handle outliers
    def outlier_treatment(of,kk):
        q1=of[kk].quantile(0.25)
        q3=of[kk].quantile(0.75)
        iqr=q3-q1
        quantiles=[q1-1.5*iqr,q3+1.5*iqr]
        return quantiles

    numeric_data=of.select_dtypes([np.number]).columns 
    
    for kk in numeric_data:
        outlier_ip=outlier_treatment(of,kk)
        of.loc[of[kk]<outlier_ip[0],kk]=outlier_ip[0]
        of.loc[of[kk]>outlier_ip[1],kk]=outlier_ip[1]

    ####imputation
    for kk in numeric_data:
        try:
            if of[kk].isnull().sum()/len(of[kk]) < 0.1:
                kk_mean=of[kk].mean()
                of[kk] =of[kk].apply(lambda x: np.where(pd.isnull(x),kk_mean,x))
        except:
            None
    return(of)

out_df = outlier(new_df)
out_df.to_csv('Cleaned_file_Ex26.csv',index=False)




def Smoothing(df,alpha):
  a=alpha
  j=0
  cols=list(df.columns)
  new_frame = pd.DataFrame()
  def smoothing_list(ActValList):
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

  for cl in cols:
    new_list = df[cl].tolist()
    if j == 0 :
      new_frame.insert(j,cl,new_list)
      j+=1
    else:
      Slist = smoothing_list(new_list)
      new_frame.insert(j,cl,Slist)
      j+=1
  return(new_frame)

  
#df2= pandas.read_csv('C:/Users/LENOVO1/Downloads/Multivariant - Goal Score in Basketball match.csv')
smooth_df=Smoothing(out_df,0.2)

smooth_df.to_csv('Smoothened_Values_Multi_5.csv',index=False)
