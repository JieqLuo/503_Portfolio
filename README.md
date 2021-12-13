This `README.md` file will be used for your mid-point writeup. Please read all instructions in the `instructions/` directory.



Since the original dataset has over 300 sellers and over 10000 specific products, the analysis focuses on the product categories which includes 74 unique categories. First, a choropleth map is used to find the overall demand distribution for each state. It can allow user to figure out the order number for a state in a specific year (right now it is based on 2018 year). Additionally, it will also allow users to know the average consumption level and total consumption level for a corresponded product categories in each state. it will provide information for users who want to get into the online shopping business and know how to allocate resources to different customers in a state. After users use the map to figure out a potential product category to begin their business, users might want to know the specific supply and demand flows among states. Therefore, a sankey diagram is provided for corresponded categories in the first map. Users can choose a specific product category to figure out the supply number and demand number flows among states. In the futures, the total revenue and average revenue per order will be tried to show. Lastly, if it is possible, a network will be used to understand customer's reviews or common online shopping characteristics for customers

For the change of vision compared to the original plan, it is hard to achieve automatically cross link function among maps. It means that only change a plot can not make other plots change at the same time. The way I know how to do it will require a server to support (dash) 
Next, I will use a bar chart which will show top sellers for a product category and the analysis will focus on the delivery efficiency, customer reviews and revenue relationships. Boxplot will used to show reviews distribution, delivery efficiency and revenue will be shown using bar chart.  Also, for a product category, week, month period demand analysis will be shown through time series line chart with a selection box. Users can easily choose a product categery and change to week or monthly period time series plot to analyze a product category. 


There is my prototype:
![alt text](https://github.com/anly503/project-fall-2021-JieqLuo/blob/b3f933c6f8cf34b5b26d9a912a9b99c13e8bc7db/prototype.jpg?raw=true)
Data Origin: https://www.kaggle.com/olistbr/brazilian-ecommerce

The mainly data preprocessing pipeline I have done can be divided to several parts. Firstly, check missing value for each datasets and find there is less than 3 % missing review values. Since it is self-selection for customers, it was not filled right now. Then, datasets except geographic information datasets were all joined together by common keys. Average consumption is generated as a new column and the states names were transfomred from abbreviation to full name. Then corresponded aggreations were run to prepare for plots building.

