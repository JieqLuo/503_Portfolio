# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:04:56 2021

@author: 78149
"""

# Standard libs
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)

import plotly.express as px
import plotly.graph_objs as go
import json

import itertools

import plotly.io as pio
pio.renderers.default = "browser"




# Reading all the files
raw_path = 'C:/Users/78149/Desktop/503/503/project/archive/'
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

# select orders whose order status is delivered 
df_1_3_4_5_6_7_8=df_1_3_4_5_6_7_8.loc[df_1_3_4_5_6_7_8.order_status=='delivered']
df_1_3_4_5_6_7_8['order_purchase_timestamp'] = pd.to_datetime(df_1_3_4_5_6_7_8['order_purchase_timestamp'])
df_1_3_4_5_6_7_8['order_approved_at'] = pd.to_datetime(df_1_3_4_5_6_7_8['order_approved_at'])
df_1_3_4_5_6_7_8['order_estimated_delivery_date'] = pd.to_datetime(df_1_3_4_5_6_7_8['order_estimated_delivery_date'])
df_1_3_4_5_6_7_8['order_delivered_customer_date'] = pd.to_datetime(df_1_3_4_5_6_7_8['order_delivered_customer_date'])
df_1_3_4_5_6_7_8['delay'] = (df_1_3_4_5_6_7_8['order_delivered_customer_date'] - df_1_3_4_5_6_7_8['order_estimated_delivery_date']).dt.total_seconds() / (3600 * 24)
df_1_3_4_5_6_7_8['deliver'] = (df_1_3_4_5_6_7_8['order_delivered_customer_date'] - df_1_3_4_5_6_7_8['order_approved_at']).dt.total_seconds() / (3600 * 24)
df_1_3_4_5_6_7_8['delay'] = df_1_3_4_5_6_7_8['delay'].fillna(0)
df_1_3_4_5_6_7_8['deliver'] = df_1_3_4_5_6_7_8['deliver'].fillna(0)
df_1_3_4_5_6_7_8['order_purchase_year'] = df_1_3_4_5_6_7_8.order_purchase_timestamp.dt.to_period('Y').astype(str)
df_1_3_4_5_6_7_8['order_purchase_date'] = df_1_3_4_5_6_7_8.order_purchase_timestamp.dt.to_period('D').astype(str)
df_1_3_4_5_6_7_8['order_purchase_month'] = df_1_3_4_5_6_7_8.order_purchase_timestamp.dt.to_period('M').astype(str)




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





f=open('C:/Users/78149/Desktop/503/503/project/archive/brazil_geo.json')
jsonstates = json.load(f)


abbrev_state={}

for diction in jsonstates['features']:
    abbrev_state[diction['properties']['name']]=diction['id']
    
abbrev = dict(map(reversed, abbrev_state.items()))


### map1  #reference:https://plotly.com/python/facet-plots/

# Data

demand_state_max_product_category_geo['full_customer_state'] = demand_state_max_product_category_geo['customer_state'].map(lambda x: abbrev[x])

demand_state_max_product_category_geo=demand_state_max_product_category_geo.loc[demand_state_max_product_category_geo.order_purchase_year=='2018']


title='Product category Consumption distribution with largest demand in each state'
demand_state_max_product_category_geo['text'] = 'State: '+demand_state_max_product_category_geo['full_customer_state'] + '<br>' +\
    'Product Category: '+demand_state_max_product_category_geo['product_category_name'].astype(str)+ '<br>'+'Order Number: '+ demand_state_max_product_category_geo['order_number'].astype(str)+' orders ' 



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
fig.show()
fig.write_html("C:/Users/78149/Desktop/503/503/project/archive/choropleth.html")





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
state_year_product_category_flow['customer_state']=state_year_product_category_flow['customer_state'].map(lambda x: abbrev[x])
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
                            ]
                
                }       
                 ]

# update layout with buttons, and show the figure
sank = genSankey(state_year_product_category_flow,cat_cols=['product_category_name','seller_state','customer_state'],value_cols='order_number_flow',title='Supply and Demand flow for Product belongs to a category in 2018')
fig = go.Figure(sank)
fig.update_layout(updatemenus=updatemenus)
fig.update_layout(
    font_family="Arial Black",
)
fig.update_layout(
    annotations=[
        dict(text=":Product category", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)


fig.write_html("C:/Users/78149/Desktop/503/503/project/archive/sankey_diagram.html")

# Use dropdown below to interact with the plot




#### map3
#month and week sales in a year

cols =list(state_year_product_category_flow['product_category_name'].unique())
sellers_revenue_prodcut_category=df_1_3_4_5_6_7_8_2018.loc[df_1_3_4_5_6_7_8_2018.product_category_name.isin(cols)]
sellers_revenue_prodcut_category=sellers_revenue_prodcut_category.groupby(['product_category_name','order_purchase_year','seller_id']).payment_value.sum().reset_index()
sellers_revenue_prodcut_category
top_sellers_index=sellers_revenue_prodcut_category.groupby(['product_category_name','order_purchase_year'])['payment_value'].nlargest(10).index
index=[top_sellers_index[i][2] for i in range(len(top_sellers_index))]

top_sellers_revenue_prodcut_category=sellers_revenue_prodcut_category.iloc[index]
top_sellers_revenue_prodcut_category.columns=['product_category_name', 'order_purchase_year', 'seller_id',
       'total_revenue_from_this_product_category']

# top_sellers_revenue_prodcut_category=sellers_revenue_prodcut_category.loc[sellers_revenue_prodcut_category.seller_id.isin(list(top_sellers_revenue_prodcut_category_original.seller_id.unique()))]
# top_sellers_revenue_prodcut_category.columns=['product_category_name', 'order_purchase_year', 'seller_id',
#        'total_revenue_from_this_product_category']
import plotly.express as px

fig = px.bar(top_sellers_revenue_prodcut_category, x='total_revenue_from_this_product_category', y='seller_id',orientation='h', title='Top sellers id sorted by revenue for the corresponded product category')
# fig.update_traces(textposition='inside', textinfo='percent+label',\
#                  hovertemplate = "Country:%{label}: <br>Population: %{value} </br>(life expentancy, iso num) : %{customdata}"
# )
# fig.update_layout(barmode='group')




cols =list(state_year_product_category_flow['product_category_name'].unique())
buttons=[]
for col in cols:
    buttons.append(dict(method = "restyle",
                    args = [{'x': [top_sellers_revenue_prodcut_category.loc[top_sellers_revenue_prodcut_category.product_category_name==col]['total_revenue_from_this_product_category'].tolist()],
                             "y": [top_sellers_revenue_prodcut_category.loc[top_sellers_revenue_prodcut_category.product_category_name==col]['seller_id'].tolist()]}],
                    label = col))
    

fig.update_layout(
                  updatemenus=[dict(active=0,
                                    buttons=buttons, xanchor='right',
                                    yanchor='bottom')
                              ]) 
fig.update_layout(
    annotations=[
        dict(text=":Product category", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)  
fig.write_html("C:/Users/78149/Desktop/503/503/project/archive/Top_seller_id_bar_plot.html")





# map 4
# show review score distribution for selected company and product
# boxplot

l=[]
for product_category in list(top_sellers_revenue_prodcut_category.product_category_name.unique()):
    print(len(top_sellers_revenue_prodcut_category.loc[top_sellers_revenue_prodcut_category.product_category_name==product_category].seller_id.unique()))
    for seller_id in list(top_sellers_revenue_prodcut_category.loc[top_sellers_revenue_prodcut_category.product_category_name==product_category].seller_id.unique()):
        l.append((product_category,seller_id))
 
frames=[]
for product_category,seller_id in l:
    df=df_1_3_4_5_6_7_8.loc[(df_1_3_4_5_6_7_8.product_category_name==product_category) &(df_1_3_4_5_6_7_8.seller_id==seller_id)]
    frames.append(df)
total_df=pd.concat(frames)

        # df_1_3_4_5_6_7_8.loc[(df_1_3_4_5_6_7_8.product_category_name==product_category) &(df_1_3_4_5_6_7_8.seller_id==seller_id)]
# re_company_df=total_df.groupby(['seller_id','product_category_name','order_purchase_month'])['order_id'].count().reset_index()
# date_order_company_df.columns=['seller_id','product_category_name','order_purchase_month','order_number']
import plotly.express as px
import pandas as pd
# date_order_company_df['seller_for_product_category']=date_order_company_df['seller_id']+'_'+date_order_company_df['product_category_name']

total_df['seller_for_product_category']=total_df['seller_id']+'_'+total_df['product_category_name']
total_df['delay_status']=total_df['delay'].apply(lambda x : 'no_delay' if x<=0 else 'delay')
fig = px.box(total_df, x='product_category_name', y='review_score',title='review score distribution of delay status for a seller and a corresponded product category')

cols =list(total_df['seller_for_product_category'].unique())
buttons=[]
for col in cols:
    buttons.append(dict(method = "restyle",
                    args = [{'x': [total_df.loc[total_df.seller_for_product_category==col]['delay_status'].tolist()],
                             "y": [total_df.loc[total_df.seller_for_product_category==col]['review_score'].tolist()]}],
                    label = col))
    

fig.update_layout(
                  updatemenus=[dict(active=0,
                                    buttons=buttons, xanchor='right',
                                    yanchor='bottom')
                              ]) 
fig.update_layout(
    annotations=[
        dict(text=":Product category", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)  

fig.write_html("C:/Users/78149/Desktop/503/503/project/archive/Top_seller_review_box_plot.html")
# map 5
# scatter plot x- delay, y-review scores legend- company+product category
# how delay affect review scores, how delay distribution for each company and product category

#https://altair-viz.github.io/gallery/scatter_with_layered_histogram.html

import altair as alt
import pandas as pd
import numpy as np

# generate fake data
# source = pd.DataFrame({'gender': ['M']*1000 + ['F']*1000,
#                'height':np.concatenate((np.random.normal(69, 7, 1000),
#                                        np.random.normal(64, 6, 1000))),
#                'weight': np.concatenate((np.random.normal(195.8, 144, 1000),
#                                         np.random.normal(167, 100, 1000))),
#                'age': np.concatenate((np.random.normal(45, 8, 1000),
#                                         np.random.normal(51, 6, 1000)))
#         })


selector = alt.selection_single(empty='all', fields=['seller_for_product_category'])

# color_scale = alt.Scale(domain=['M', 'F'],
#                         range=['#1FC3AA', '#8624F5'])

base = alt.Chart(total_df).properties(
    width=250,
    height=250
).add_selection(selector)

points = base.mark_point(filled=True, size=200).encode(
    x=alt.X('mean(delay):Q',
            scale=alt.Scale(domain=[-20,5])),
    y=alt.Y('mean(review_score):Q',
            scale=alt.Scale(domain=[0,6])),
    color=alt.condition(selector,
                        'seller_for_product_category:N',
                        alt.value('lightgray'),legend=alt.Legend(columns=2, symbolLimit=0)),
    tooltip=['seller_for_product_category', 'mean(delay)', 'mean(review_score)']
)

hists = base.mark_line(opacity=0.5, thickness=100).encode(
    x=alt.X('delay:Q',
            bin=alt.Bin(step=-1), # step keeps bin size the same
            scale=alt.Scale(domain=[0,6])),
    y=alt.Y('count()',
            stack=None,
            scale=alt.Scale(domain=[0,1000])),
    color=alt.Color('seller_for_product_category:N'
                    ),
        tooltip=['seller_for_product_category', 'delay', 'count()']
).transform_filter(
    selector
)

chart=alt.vconcat(
    points,
    hists,
    data=total_df,
    title="review score and delay data distribution for each top seller "
)

chart.save('C:/Users/78149/Desktop/503/503/project/archive/scatter_barplot.html')
