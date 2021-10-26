# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 00:56:56 2021

@author: 78149
"""

#####################
import altair as alt
import pandas as pd
import os
import datetime
import glob

# households=['04','05','06']

# def convert(n):
#     return str(datetime.timedelta(seconds = n))
# original_path=os.getcwd()
# final_dataframe=pd.DataFrame(columns=['date','weekday','day','month',"household","consumption","consumption_type"])
# for household in households:
#     abs_path=original_path+'\\'+'eco'+'\\'+household
#     os.chdir(abs_path)
#     if household =='04':
#         folder_level_one=['01','02','03','04','05','06','07','08']
#         column_map={'01':"Fridge",'02':"Kitchen appliances",'03':"Lamp",'04':"Stereo and laptop",'05':"Freezer",'06':"Tablet",'07':"Entertainment",'08':"Microwave"}
#     elif household =='05':
#         folder_level_one=['01','02','03','04','05','06','07','08']
#         column_map={'01':"Tablet",'02':"Coffee machine",'03':"Fountain",'04':"Microwave",'05':"Fridge",'06':"Entertainment",'07':"PC",'08':"Kettle"}
#     else:
#         folder_level_one=['01','02','03','04','05','06','07']
#         column_map={'01':"Lamp",'02':"Laptop",'03':"Router",'04':"Coffee machine",'05':"Entertainment",'06':"Fridge",'07':"Kettle"}            
#     final_glued_data = pd.DataFrame(columns=['date','weekday','day','month',"household","consumption","consumption_type"])
#     for column in folder_level_one:
#         path=os.getcwd()+ "\\" + column + "\\"
#         csv_files= glob.glob(os.path.join(path,"*.csv"))
#         glued_data = pd.DataFrame(columns=['consumption','date'])    
#         for f in csv_files:
#             df = pd.read_csv(f,header=None)
#             print('Location:', f)
#             file_name=f.split("\\")[-1]
#             print('File Name:',file_name)
#             date=file_name.split(".")[0]
#             df['date']=datetime.datetime.strptime(date, '%Y-%m-%d')
#             df['weekday']=datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
#             df['day']=datetime.datetime.strptime(date, '%Y-%m-%d').day
#             df['month']=datetime.datetime.strptime(date, '%Y-%m-%d').month       
#             df_modified=df.reset_index()  

#             df_modified.columns=['time','consumption','date','weekday','day','month']

#             df_modified["time"] = df_modified["time"].apply(lambda x : convert(int(x)))
#             df_modified["household"]=household
#             df_modified=df_modified.loc[df_modified.consumption>=0]
#             df_final=df_modified.groupby(['household','date','weekday','day','month'])['consumption'].sum().reset_index()
#             df_final['consumption_type']=column_map[column]
#             print(df_final)
#             glued_data=pd.concat([glued_data,df_final],axis=0)
#             # print the content
#             print('Content:')
#             print(df.dtypes)
#         final_glued_data=pd.concat([final_glued_data,glued_data],axis=0)
    
#     final_dataframe=pd.concat([final_dataframe,final_glued_data],axis=0)
    
    

source = pd.read_csv('combined_df.csv')


# scale = alt.Scale(domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
#                   range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd'])
# color = alt.Color('consumption_type:N', scale=scale)
color = alt.Color('consumption_type:N')
# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])
# input_dropdown = alt.binding_select(options=['Coffee machine','Entertainment','Fountain','Freezer','Fridge','Kettle','Kitchen appliances','Lamp','Laptop','Microwave','PC','Router','Stereo and laptop','Tablet'])
# input_dropdown = alt.binding_select(options=['04','05','06']
# selection = alt.selection_single(fields=['household'], bind=input_dropdown, name='householder')
radio_select = alt.selection_multi(fields=["consumption_type"], name="consumption_type", 
    )
# Top panel is scatter plot of temperature vs time
points = alt.Chart(source).mark_line().encode(
    alt.X('date:T', title='Date'),
    alt.Y('consumption:Q',
        title='power consumption (hz*second))'
    ),
    color=alt.condition(click, color, alt.value('lightgray')),
    facet=alt.Facet('household:N', columns =3),
    title="Line Chart of Consumption for Each Plug Function in Each Household",
    tooltip = [alt.Tooltip('household:N'),
               alt.Tooltip('date:T'),
               alt.Tooltip('consumption_type:N'),
               alt.Tooltip('consumption:Q')
              ]
).properties(
    width='container',
    height=300
).add_selection(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of weather type
bars = alt.Chart(source).mark_bar().encode(
    x='sum(consumption)',
    y='household:N',
    color=alt.condition(click, color, alt.value('lightgray')),
    title="Power Consumption for 3 Households "
).transform_filter(
    brush
).properties(
    width=550,
).add_selection(
    click
)

chart=alt.vconcat(
    points,
    bars,
    data=source,
    title="Power Consumption for 3 Households from 2012-06-27 to 2013-01-31"
)

chart.save('example.html')

#https://altair-viz.github.io/user_guide/interactions.html