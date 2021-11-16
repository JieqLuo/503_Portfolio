# -*- coding: utf-8 -*-




import pandas as pd
import numpy as np
import matplotlib as plt
import datetime
import os 
import glob

households=['04','05','06']

def convert(n):
    return str(datetime.timedelta(seconds = n))
original_path=os.getcwd()
final_dataframe=pd.DataFrame(columns=['date','weekday','day','month',"household","consumption","consumption_type"])
for household in households:
    abs_path=original_path+'\\'+'eco'+'\\'+household
    os.chdir(abs_path)
    if household =='04':
        folder_level_one=['01','02','03','04','05','06','07','08']
        column_map={'01':"Fridge",'02':"Kitchen appliances",'03':"Lamp",'04':"Stereo and laptop",'05':"Freezer",'06':"Tablet",'07':"Entertainment",'08':"Microwave"}
    elif household =='05':
        folder_level_one=['01','02','03','04','05','06','07','08']
        column_map={'01':"Tablet",'02':"Coffee machine",'03':"Fountain",'04':"Microwave",'05':"Fridge",'06':"Entertainment",'07':"PC",'08':"Kettle"}
    else:
        folder_level_one=['01','02','03','04','05','06','07']
        column_map={'01':"Lamp",'02':"Laptop",'03':"Router",'04':"Coffee machine",'05':"Entertainment",'06':"Fridge",'07':"Kettle"}            
    final_glued_data = pd.DataFrame(columns=['date','weekday','day','month',"household","consumption","consumption_type"])
    for column in folder_level_one:
        path=os.getcwd()+ "\\" + column + "\\"
        csv_files= glob.glob(os.path.join(path,"*.csv"))
        glued_data = pd.DataFrame(columns=['consumption','date'])    
        for f in csv_files:
            df = pd.read_csv(f,header=None)
            print('Location:', f)
            file_name=f.split("\\")[-1]
            print('File Name:',file_name)
            date=file_name.split(".")[0]
            df['date']=datetime.datetime.strptime(date, '%Y-%m-%d')
            df['weekday']=datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
            df['day']=datetime.datetime.strptime(date, '%Y-%m-%d').day
            df['month']=datetime.datetime.strptime(date, '%Y-%m-%d').month       
            df_modified=df.reset_index()  

            df_modified.columns=['time','consumption','date','weekday','day','month']

            df_modified["time"] = df_modified["time"].apply(lambda x : convert(int(x)))
            df_modified["household"]=household
            df_modified=df_modified.loc[df_modified.consumption>=0]
            df_final=df_modified.groupby(['household','date','weekday','day','month'])['consumption'].sum().reset_index()
            df_final['consumption_type']=column_map[column]
            print(df_final)
            glued_data=pd.concat([glued_data,df_final],axis=0)
            # print the content
            print('Content:')
            print(df.dtypes)
        final_glued_data=pd.concat([final_glued_data,glued_data],axis=0)
    
    final_dataframe=pd.concat([final_dataframe,final_glued_data],axis=0)
    
final_dataframe.to_csv('combined_df.csv',index=False)



