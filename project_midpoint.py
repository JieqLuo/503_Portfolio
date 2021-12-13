# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:04:56 2021

@author: 78149
"""

# Standard libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.gridspec import GridSpec
pd.set_option('display.max_columns', 100)
import plotly.offline as py
import plotly.express as px
import plotly.graph_objs as go
import json
import requests
import itertools

import plotly.io as pio
pio.renderers.default = "browser"

# DataPrep
import re
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import joblib



# Reading all the files
raw_path = 'C:/Users/78149/Desktop/503/project/archive/'
olist_customer = pd.read_csv(raw_path + 'olist_customers_dataset.csv')
olist_geolocation = pd.read_csv(raw_path + 'olist_geolocation_dataset.csv')
olist_orders = pd.read_csv(raw_path + 'olist_orders_dataset.csv')
olist_order_items = pd.read_csv(raw_path + 'olist_order_items_dataset.csv')
olist_order_payments = pd.read_csv(raw_path + 'olist_order_payments_dataset.csv')
olist_order_reviews = pd.read_csv(raw_path + 'olist_order_reviews_dataset.csv')
olist_products = pd.read_csv(raw_path + 'olist_products_dataset.csv')
olist_sellers = pd.read_csv(raw_path + 'olist_sellers_dataset.csv')


olist_customer.info()
olist_geolocation.info()
olist_orders.info()
olist_order_items.info()
olist_order_payments.info()
olist_order_reviews.info()
olist_products.info()
olist_sellers.info()



print(olist_customer.isnull().sum())
print(olist_geolocation.isnull().sum())
print(olist_orders.isnull().sum())
print(olist_order_items.isnull().sum())
print(olist_order_payments.isnull().sum())
print(olist_order_reviews.isnull().sum())
print(olist_products.isnull().sum())
print(olist_sellers.isnull().sum())

# remove duplicates 
olist_customer=olist_customer.drop_duplicates('customer_id',False)
olist_orders=olist_orders.drop_duplicates('order_id',False)
olist_products=olist_products.drop_duplicates('product_id',False)
olist_sellers=olist_sellers.drop_duplicates('seller_id',False)

df_3_4=pd.merge(olist_orders,
                 olist_order_items,
                 on='order_id')
df_3_4_5=pd.merge(df_3_4,
                 olist_order_payments,
                 on='order_id')
df_3_4_5_6=pd.merge(df_3_4_5,
                 olist_order_reviews,
                 on='order_id')

df_3_4_5_6_7=pd.merge(df_3_4_5_6,
                 olist_products,
                 on='product_id')
df_3_4_5_6_7_8=pd.merge(df_3_4_5_6_7,
                 olist_sellers,
                 on='seller_id')

df_1_3_4_5_6_7_8=pd.merge(df_3_4_5_6_7_8,
                 olist_customer,
                 on='customer_id')

df_1_3_4_5_6_7_8.product_category_name.unique().shape[0]
df_1_3_4_5_6_7_8.product_id.unique().shape[0]
df_1_3_4_5_6_7_8.seller_id.unique().shape[0]



df_1_3_4_5_6_7_8.order_purchase_timestamp = pd.to_datetime(df_1_3_4_5_6_7_8.order_purchase_timestamp)
df_1_3_4_5_6_7_8.order_approved_at = pd.to_datetime(df_1_3_4_5_6_7_8.order_approved_at)
df_1_3_4_5_6_7_8.order_estimated_delivery_date = pd.to_datetime(df_1_3_4_5_6_7_8.order_estimated_delivery_date)
df_1_3_4_5_6_7_8.order_delivered_customer_date = pd.to_datetime(df_1_3_4_5_6_7_8.order_delivered_customer_date)
df_1_3_4_5_6_7_8.review_creation_date = pd.to_datetime(df_1_3_4_5_6_7_8.review_creation_date)
df_1_3_4_5_6_7_8.review_answer_timestamp = pd.to_datetime(df_1_3_4_5_6_7_8.review_answer_timestamp)

df_1_3_4_5_6_7_8['order_purchase_year'] = df_1_3_4_5_6_7_8.order_purchase_timestamp.dt.to_period('Y').astype(str)


#map 1
#get product_category with largest demand in each state
state_year_product_category=df_1_3_4_5_6_7_8.groupby(['customer_state','order_purchase_year','product_category_name']).order_id.count().reset_index()
state_year_product_category.columns=['customer_state','order_purchase_year','product_category_name','order_number']
demand_state_max_product_category=state_year_product_category.groupby(['customer_state','order_purchase_year']).apply(lambda df: df.loc[df.order_number.idxmax()])
demand_state_max_product_category=demand_state_max_product_category.reset_index(drop=True)

#combined with geo_information_dataframe
olist_geolocation['customer_state']=olist_geolocation['geolocation_state']
demand_state_max_product_category_geo=pd.merge(demand_state_max_product_category,
                                               olist_geolocation,
                                               on='customer_state')





demand_state_product_category_number_value= pd.merge(df_1_3_4_5_6_7_8, demand_state_max_product_category,  how='inner', left_on=['customer_state','order_purchase_year','product_category_name'], right_on = ['customer_state','order_purchase_year','product_category_name'])


demand_state_product_category_number_value=demand_state_product_category_number_value.groupby(['customer_state','order_purchase_year','product_category_name']).payment_value.sum().reset_index()
demand_state_product_category_number_value.columns=['customer_state','order_purchase_year','product_category_name','total_consumption']

demand_state_product_category_number_value=demand_state_product_category_number_value.groupby(['customer_state','order_purchase_year']).apply(lambda df: df.loc[df.total_consumption.idxmax()])
demand_state_product_category_number_value=demand_state_product_category_number_value.reset_index(drop=True)
demand_state_product_category_number_value=pd.merge(demand_state_product_category_number_value, demand_state_max_product_category,  how='inner', left_on=['customer_state','order_purchase_year','product_category_name'], right_on = ['customer_state','order_purchase_year','product_category_name'])


demand_state_product_category_number_value['average_comsuption_unit_order']=demand_state_product_category_number_value.total_consumption/demand_state_product_category_number_value.order_number


#combined with geo_information_dataframe
olist_geolocation['customer_state']=olist_geolocation['geolocation_state']
demand_state_max_product_category_geo=demand_state_product_category_number_value.copy()





f=open('C:/Users/78149/Desktop/503/project/archive/brazil_geo.json')
jsonstates = json.load(f)


abbrev_state={}

for diction in jsonstates['features']:
    abbrev_state[diction['properties']['name']]=diction['id']
    
abbrev = dict(map(reversed, abbrev_state.items()))


### map1  #reference:https://plotly.com/python/facet-plots/

# Data

demand_state_max_product_category_geo['full_customer_state'] = demand_state_max_product_category_geo['customer_state'].map(lambda x: abbrev[x])

demand_state_max_product_category_geo=demand_state_max_product_category_geo.loc[demand_state_max_product_category_geo.order_purchase_year=='2018']
# # define traces and buttons at once
# traces = []
# buttons = []
# for value in cols_dd:
#     traces.append(go.Choropleth(
#             geojson=jsonstates,
#             z=demand_state_max_product_category_geo[value].astype(float), # Data to be color-coded
#             colorbar_title=value,
#             visible= True if value==cols_dd[0] else False))
    
#     buttons.append(dict(label=value,
#                         method="update",
#                         args=[{"visible":list(visible==value)},
#                               {"title":f"<b>{value}</b>"}]))

# updatemenus = [{"active":0,
#                 "buttons":buttons,
#                }]


# # Show figure
# fig = go.Figure(data=traces,
#                 layout=dict(updatemenus=updatemenus))
# # This is in order to get the first title displayed correctly
# first_title = cols_dd[0]
# fig.update_layout(title=f"<b>{first_title}</b>",title_x=0.5)
# fig.show()

title='Product category Consumption distribution with largest demand in each state'
demand_state_max_product_category_geo['text'] = 'State: '+demand_state_max_product_category_geo['full_customer_state'] + '<br>' +\
    'Product Category: '+demand_state_max_product_category_geo['product_category_name'].astype(str)+ '<br>'+'Order Number: '+ demand_state_max_product_category_geo['order_number'].astype(str)+' orders ' 

# # demand_state_max_product_category_geo["order_purchase_year"]=demand_state_max_product_category_geo["order_purchase_year"].astype(int)
# fig=px.scatter_geo(demand_state_max_product_category_geo,  
#                         geojson=jsonstates,
#                         locations='full_customer_state',                           
#                         featureidkey='properties.name',
#                         hover_name= 'text',
#                         # color="product_category_name",                        
#                         size='order_number',
#                         hover_data={'order_number':False,'full_customer_state':False},
#                         animation_frame="order_purchase_year",
#                         title='Product category distribution with largest demand in each state '
#                     )

cols_dd = ["order_number", "total_consumption", "average_comsuption_unit_order"]
layout=go.Layout(title=title)
fig = go.Figure(layout=layout)
for i, value in enumerate(cols_dd):
    ca = f"coloraxis{i+2}"
    figc = px.choropleth(demand_state_max_product_category_geo, geojson=jsonstates, 
                                locations='full_customer_state',                           
                                color=value,
                                featureidkey='properties.name',
                                color_continuous_scale='spectral_r',
                                # projection='albers usa',
                                # locationmode="USA-states",
                                hover_name= 'text',
                                animation_frame="order_purchase_year",
                                # labels={'Value':'total commodity value/Million$'},
                                title='Product category distribution with largest demand in each state'
                              ).update_traces(visible=False, coloraxis=ca)
    fig = fig.add_traces(figc.data)
    fig = fig.update_layout(
    {
        ca: {
            "cmin": demand_state_max_product_category_geo[value].replace(0, np.nan).quantile(0.25),
            "cmax": demand_state_max_product_category_geo[value].replace(0, np.nan).quantile(0.75),
            "colorbar": {"title": value},
        }
    })
    
fig.update_geos(fitbounds="locations")
fig.update_layout(

    updatemenus=[
        {
            "buttons": [
                {
                    "label": f"{m}",
                    "method": "update",
                    "args": [
                        {
                            "visible": [
                                (m2 == m and p2 == p)
                                for m2, p2 in itertools.product(
                                    cols_dd, ["choropleth"]
                                )
                            ]
                        },
                        {"title": f"<b>{m}</b>"},
                    ],
                }
                for m, p in itertools.product(cols_dd, ["choropleth"])
            ]
        
        },
        
        
        
    ],
    
    margin={"l": 0, "r": 0, "t": 25, "b": 0}
)
fig.write_html("C:/Users/78149/Desktop/503/project/archive/choropleth.html")




# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# import itertools

# # get OWID data
# df = pd.read_csv(
#     "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
# )
# # rename columns as sample code uses other names....
# df = df.rename(
#     columns={
#         "location": "Location",
#         "iso_code": "Iso code",
#         "total_tests": "Total tests",
#         "people_vaccinated_per_hundred": "Vaccines",
#         "new_cases": "Recent cases",
#         "total_cases": "Total cases",
#         "total_deaths": "Total deaths",
#         "total_vaccinations": "Total vaccinations",
#         "people_vaccinated": "People vaccinated",
#         "population": "Population",
#         "total_boosters": "Vaccination policy",
#     }
# ).fillna(0)
# cols_dd = ["Total tests", "Total cases", "Total deaths", "Recent cases", "new_deaths"]
# hd = {
#     "Iso code": False,
#     "Vaccines": True,
#     "Total tests": ": ,0.f",
#     "Recent cases": ": ,0.f",
#     "Total cases": ": ,0.f",
#     "Total deaths": ": ,0.f",
#     "Total vaccinations": ": ,0.f",
#     "People vaccinated": ": ,0.f",
#     "Population": ": ,0.f",
#     "Vaccination policy": ": 0.f",
# }

# fig = go.Figure()

# for i, value in enumerate(cols_dd):
#     # use a different color axis for each trace... makes it more responsive
#     ca = f"coloraxis{i+2}"

#     figc = px.choropleth(
#         df,
#         locations="Iso code",  # Spatial coordinates
#         color=value,  # Data to be color-coded
#         hover_data=hd,
#         color_continuous_scale="spectral_r",
#         hover_name="Location",
#     ).update_traces(visible=False, coloraxis=ca)
#     figs = px.scatter_geo(
#         df,
#         locations="Iso code",  # Spatial coordinates
#         color=value,  # Data to be color-coded
#         hover_data=hd,
#         color_continuous_scale="spectral_r",
#         hover_name="Location",
#     ).update_traces(visible=False, marker={"coloraxis": ca})

#     fig = fig.add_traces(figc.data)
#     fig = fig.add_traces(figs.data)
#     fig = fig.update_layout(
#         {
#             ca: {
#                 "cmin": df[value].replace(0, np.nan).quantile(0.25),
#                 "cmax": df[value].replace(0, np.nan).quantile(0.75),
#                 "colorbar": {"title": value},
#             }
#         }
#     )


# fig.update_layout(
#     updatemenus=[
#         {
#             "buttons": [
#                 {
#                     "label": f"{m} - {p}",
#                     "method": "update",
#                     "args": [
#                         {
#                             "visible": [
#                                 (m2 == m and p2 == p)
#                                 for m2, p2 in itertools.product(
#                                     cols_dd, ["choropleth", "scatter"]
#                                 )
#                             ]
#                         },
#                         {"title": f"<b>{m}</b>"},
#                     ],
#                 }
#                 for m, p in itertools.product(cols_dd, ["choropleth", "scatter"])
#             ]
#         }
#     ],
#     margin={"l": 0, "r": 0, "t": 25, "b": 0},
# )

# fig.show()


# # This is in order to get the first title displayed correctly
# first_title = cols_dd[0]
# fig.update_layout(title=f"<b>{first_title}</b>",title_x=0.5)
# fig.show()


#map 2
#sankey diagram
df_1_3_4_5_6_7_8_2018=df_1_3_4_5_6_7_8.loc[df_1_3_4_5_6_7_8.order_purchase_year=='2018']
state_year_product_category=df_1_3_4_5_6_7_8_2018.groupby(['customer_state','seller_state','order_purchase_year','product_category_name']).order_id.count().reset_index()
state_year_product_category.columns=['customer_state','seller_state','order_purchase_year','product_category_name','order_number_flow']


state_year_product_category_flow= pd.merge(state_year_product_category, demand_state_max_product_category,  how='inner', left_on=['customer_state','order_purchase_year','product_category_name'], right_on = ['customer_state','order_purchase_year','product_category_name'])


state_year_product_category_flow=state_year_product_category_flow.reset_index(drop=True)

# Helper function to transform regular data to sankey format
# Returns data and layout as dictionary
def genSankey(df,cat_cols=[],value_cols='',title='Sankey Diagram'):
    # maximum of 6 value cols -> 6 colors
    colorPalette = ['#4B8BBE','#306998','#FFE873','#FFD43B','#646464']
    labelList = []
    colorNumList = []
    for catCol in cat_cols:
        labelListTemp =  list(set(df[catCol].values))
        colorNumList.append(len(labelListTemp))
        labelList = labelList + labelListTemp
        
    # remove duplicates from labelList
    labelList = list(dict.fromkeys(labelList))
    
    # define colors based on number of levels
    colorList = []
    for idx, colorNum in enumerate(colorNumList):
        colorList = colorList + [colorPalette[idx]]*colorNum
        
    # transform df into a source-target pair
    for i in range(len(cat_cols)-1):
        if i==0:
            sourceTargetDf = df[[cat_cols[i],cat_cols[i+1],value_cols]]
            sourceTargetDf.columns = ['source','target','count']
        else:
            tempDf = df[[cat_cols[i],cat_cols[i+1],value_cols]]
            tempDf.columns = ['source','target','count']
            sourceTargetDf = pd.concat([sourceTargetDf,tempDf])
        sourceTargetDf = sourceTargetDf.groupby(['source','target']).agg({'count':'sum'}).reset_index()
        
    # add index for source-target pair
    sourceTargetDf['sourceID'] = sourceTargetDf['source'].apply(lambda x: labelList.index(x))
    sourceTargetDf['targetID'] = sourceTargetDf['target'].apply(lambda x: labelList.index(x))
    
    # creating the sankey diagram
    data = dict(
        type='sankey',
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(
            color = "black",
            width = 0.5
          ),
          label = labelList,
          color = colorList
        ),
        link = dict(
          source = sourceTargetDf['sourceID'],
          target = sourceTargetDf['targetID'],
          value = sourceTargetDf['count']
        )
      )
    
    layout =  dict(
        title = title,
        font = dict(
          size = 10
        )
    )
       
    fig = dict(data=[data], layout=layout)
    return fig


# Generating DFs for different filter options

state_year_product_category_flow['seller_state']=state_year_product_category_flow['seller_state'].map(lambda x: abbrev[x])
state_year_product_category_flow['customer_state']=state_year_product_category_flow['customer_state'].apply(lambda x : 'demand_state: ' +x)
state_year_product_category_flow['seller_state']=state_year_product_category_flow['seller_state'].apply(lambda x : 'supply_state: ' +x)
moveis_decoracao =  genSankey(state_year_product_category_flow[state_year_product_category_flow['product_category_name']=='moveis_decoracao'],cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')

beleza_saude =  genSankey(state_year_product_category_flow[state_year_product_category_flow['product_category_name']=='beleza_saude'],cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')


esporte_lazer =  genSankey(state_year_product_category_flow[state_year_product_category_flow['product_category_name']=='esporte_lazer'],cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')


cama_mesa_banho =  genSankey(state_year_product_category_flow[state_year_product_category_flow['product_category_name']=='cama_mesa_banho'],cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')


informatica_acessorios =  genSankey(state_year_product_category_flow[state_year_product_category_flow['product_category_name']=='informatica_acessorios'],cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')

all_product_categories=genSankey(state_year_product_category_flow,cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')
# Constructing menus
updatemenus = [{'buttons': [{'method': 'animate',
                             'label': 'all product categories',
                             'args': [all_product_categories]
                              },
                            {'method': 'animate',
                             'label': 'moveis_decoracao',
                             'args': [moveis_decoracao]
                              },
                            {'method': 'animate',
                             'label': 'beleza_saude',
                             'args': [beleza_saude]
                             },
                            {'method': 'animate',
                             'label': 'esporte_lazer',
                             'args': [esporte_lazer]
                             },
                             {'method': 'animate',
                             'label': 'cama_mesa_banho',
                             'args': [cama_mesa_banho]
                             },
                             {'method': 'animate',
                             'label': 'informatica_acessorios',
                             'args': [informatica_acessorios]
                             }
                            ] } ]

# update layout with buttons, and show the figure
sank = genSankey(state_year_product_category_flow,cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')
fig = go.Figure(sank)
fig.update_layout(updatemenus=updatemenus)
fig.write_html("C:/Users/78149/Desktop/503/project/archive/sankey_diagram.html")

# Use dropdown below to interact with the plot

#### map3
#month and week sales in a year

sellers_revenue_prodcut_category=df_1_3_4_5_6_7_8_2018.groupby(['product_category_name','order_purchase_year','seller_id']).payment_value.sum().reset_index()
top_sellers_index=sellers_revenue_prodcut_category.groupby(['product_category_name','order_purchase_year'])['payment_value'].nlargest(10).index
index=[top_sellers_index[i][2] for i in range(len(top_sellers_index))]
top_sellers_revenue_prodcut_category=sellers_revenue_prodcut_category.iloc[index]
top_sellers_revenue_prodcut_category.columns=['product_category_name', 'order_purchase_year', 'seller_id',
       'total_revenue_from_this_product_category']










# fig = go.Figure()

# colors = [
#     '#1f77b4',  # muted blue
#     '#ff7f0e',  # safety orange
#     '#2ca02c',  # cooked asparagus green
#     '#d62728',  # brick red
#     '#9467bd',  # muted purple
#     '#8c564b',  # chestnut brown
#     '#e377c2',  # raspberry yogurt pink
#     '#7f7f7f',  # middle gray
#     '#bcbd22',  # curry yellow-green
#     '#17becf'  ] # blue-teal

# fig.add_trace(go.Bar(
#         x = top_sellers_revenue_prodcut_category['total_revenue_from_this_product_category'],
#         y = top_sellers_revenue_prodcut_category['seller_id'],
#         marker_color=colors
#         ))




# # some adjustments to the updatemenu
# # from code by vestland
# updatemenu=[]
# your_menu=dict()
# updatemenu.append(your_menu)
# updatemenu[0]['buttons']=buttons
# updatemenu[0]['direction']='down'
# updatemenu[0]['showactive']=True

# fig.update_layout(updatemenus=updatemenu)

# fig.show()


# import plotly.graph_objects as px
# import numpy
  
  
# # creating random data through randomint
# # function of numpy.random
# np.random.seed(42)
  
# random_x = np.random.randint(1, 101, 100)
# random_y = np.random.randint(1, 101, 100)
  
# x = ['A', 'B', 'C', 'D']
# i=0
# for category in state_year_product_category_flow['product_category_name'].unique():  
#     top_sellers_revenue_prodcut_category_filtered=top_sellers_revenue_prodcut_category.loc[top_sellers_revenue_prodcut_category.product_category_name==category]
#     fig.add_trace(go.Bar(
#             x = top_sellers_revenue_prodcut_category_filtered['seller_id'],
#             y = top_sellers_revenue_prodcut_category_filtered['total_revenue_from_this_product_category']
#             ))
#     i+=1



# import pandas as pd 
# df = pd.DataFrame({"Date":["2020-01-27","2020-02-27","2020-03-27","2020-04-27", "2020-05-27", "2020-06-27", "2020-07-27",
#                           "2020-01-27","2020-02-27","2020-03-27","2020-04-27", "2020-05-27", "2020-06-27", "2020-07-27"],
#                    "A_item":[2, 8, 0, 1, 8, 10, 4, 7, 2, 15, 5, 12, 10, 7],
#                    "B_item":[1, 7, 10, 6, 5, 9, 2, 5, 6, 1, 2, 6, 15, 8],
#                    "C_item":[9, 2, 9, 3, 9, 18, 7, 2, 8, 1, 2, 8, 1, 3],
#                    "Channel_type":["Chanel_1", "Chanel_1", "Chanel_1", "Chanel_1", "Chanel_1", "Chanel_1", "Chanel_1", 
#                                    "Chanel_2", "Chanel_2", "Chanel_2", "Chanel_2", "Chanel_2", "Chanel_2", "Chanel_2"]
#                    })


import plotly.express as px

fig = px.bar(top_sellers_revenue_prodcut_category, y='total_revenue_from_this_product_category', x='seller_id')

# fig.update_layout(barmode='group')


fig.show()

cols =list(state_year_product_category_flow['product_category_name'].unique())
buttons=[]
for col in cols:
    buttons.append(dict(method = "restyle",
                    args = [{'y': top_sellers_revenue_prodcut_category.loc[top_sellers_revenue_prodcut_category.product_category_name==col]['total_revenue_from_this_product_category']}],
                    label = col))

fig.update_layout(height=450,
                  updatemenus=[dict(active=0,
                                    buttons=buttons)
                              ]) 
# # Add dropdown
# plot.update_layout(
#     updatemenus=[
#         dict(
#             active=0,
#             buttons=list([
#                 dict(label="Both",
#                      method="update",
#                      args=[{"visible": [True, True]},
#                            {"title": "Both"}]),
#                 dict(label="Data 1",
#                      method="update",
#                      args=[{"visible": [True, False]},
#                            {"title": "Data 1",
#                             }]),
#                 dict(label="Data 2",
#                      method="update",
#                      args=[{"visible": [False, True]},
#                            {"title": "Data 2",
#                             }]),
#             ]),
#         )
#     ])
  
fig.show()


#### map4

from plotly import graph_objs as go
import ipywidgets as w
from IPython.display import display
import pandas as pd 

fig = go.Figure()

for column in top_sellers_revenue_prodcut_category.columns.to_list():
    fig.add_trace(
        go.Bar(
            x = df_stocks.index,
            y = df_stocks[column],
            name = column
        )
    )
    
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label = 'All',
                  method = 'update',
                  args = [{'visible': [True, True, True, True]},
                          {'title': 'All',
                            'showlegend':True}]),
              dict(label = 'MSFT',
                  method = 'update',
                  args = [{'visible': [True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'MSFT',
                            'showlegend':True}]),
              dict(label = 'AAPL',
                  method = 'update',
                  args = [{'visible': [False, True, False, False]},
                          {'title': 'AAPL',
                            'showlegend':True}]),
              dict(label = 'AMZN',
                  method = 'update',
                  args = [{'visible': [False, False, True, False]},
                          {'title': 'AMZN',
                            'showlegend':True}]),
              dict(label = 'GOOGL',
                  method = 'update',
                  args = [{'visible': [False, False, False, True]},
                          {'title': 'GOOGL',
                            'showlegend':True}]),
            ])
        )
    ])

fig.show()













