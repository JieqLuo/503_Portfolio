# Overview
With development of e-commerce, online shopping has become a main way for people to purchase items. There is a lot of data produced every second for online shopping stores. Data analysis has become an important aspect for stores to improve their service and profit without taking much cost compared with the off-line stores. How to utilize data created from internet and what information a store can gain from produced data to improve itself become attractive. For instances, data allows online merchants to learn purchase preferences to improve revenue and customers satisfaction. Data can assist sellers comprehensively know shopping preference for customers and improve service quality for customer. Overall, data help business to achieve win-win between merchants and customers. The project chooses a Brazilian online shopping platform to display how merchants can get benefit from data produced from e-commerce. It includes to analyze data to provide insights for merchants to improve their sales and services. Data visualizations will be created to allow each merchant to learn the real-time trend for the whole market, details for correspond sellers’ business performance for a certain period and feedback from customers. 

# Visualization
Before getting into a market, demand is the first factor every future merchant must consider. Analyzing demand for each state can provide significant information for people who want to get into online shopping using Brazil as the platform. Therefore, the first visualization was built

## Choropleth Visualization
![choropleth](https://user-images.githubusercontent.com/68412645/145749313-3fbb76fd-a3c0-4a16-8201-354fca831246.png)

Users could explore demand (order number) distribution, total consumption (unit is million $) and unit consumption (unit is $ per order) distribution for each state, the visualization could show the corresponded top product category and specific value, corresponded state. Notice: User need to activate visualization through clicking one of option in the left top selection box otherwise the map will show nothing

Notice: User need to activate visualization through clicking one of option in the left top selection box otherwise the map will show nothing

From the demand distribution of product categories, east coast and south coast part of Brazil had much higher online demand compared to inner states. The possible reasons might be as follows. Firstly, economical level in east coast and south coast states were higher than inner states. Secondly, sellers mainly located in east coast states and south coast states. It could deliver products more efficiently to customers. Thirdly, transportation in east states and south coast states was better developed compared to inner states. The third reason can be verified from unit order consumption, customers from inner states had much higher value compared to states in east coast and south coast.

In order to verify possible findings from the first visualization and further help future sellers to select product categories, the Sankey diagram is used to show how product categories flows among states including supply and demand. Potential users can first click the selection box to choose a specific product category to find how supply and demand flow.

## Sankey Diagram
![Sankey diagram](https://user-images.githubusercontent.com/68412645/145749316-e61069aa-ec87-44b7-a151-8350bee4202a.png)

Users could specify a product category you find in the choropleth visualization; the Sankey diagram will show the corresponded supply and demand flow between states. When users move the mouse to the flow between two states, there will show the original state name, the target state name and the corresponded revenue value.

Notice: User need to activate visualization through clicking one of option in the left top selection box otherwise the Sankey diagram will show all product categories and corresponded flows

The Sankey diagram provide significant suggestions for potential sellers to decide which product categories they can choose according to their own locations to decrease delivery cost and improve delivery efficiency. Why they need to improve delivery efficiency. It will be answers in the following visualizations.

Once future sellers have interests in several product categories, it is necessary to learn top sellers in corresponded product categories. The third visualization allows potential users to find top sellers in 2018 for top product categories found in the first visualization.

## Bar Chart
![barplot](https://user-images.githubusercontent.com/68412645/145749326-d9f42d91-abce-472c-a992-a1a1ec8ec9da.png)

Users could explore top revenue sellers for top product category with highest demand in each state. When users move the mouse to a bar, corresponded revenue value and seller id will be shown. Users could change product category with the selection box on the left top.

Notice: User need to activate visualization through clicking one of option in the left top selection box otherwise the bar chart will show all top sellers for all top product categories.

After that, future sellers could have a deeper understanding for these sellers’ performance according to the customer satisfaction and delivery efficiency.

## Boxplot
![boxplot](https://user-images.githubusercontent.com/68412645/145749332-97d80d33-ef94-475e-9eab-ea60a7dd7238.png)

Users could explore review score distribution for top sellers corresponded to the top product category. Each box plot shows review score distribution for delayed orders and no-delayed orders. When users move the mouse to a box plot, corresponded median value, maximum and minimum value will be shown. Users could change sellers with the selection box on the left top.

Notice: User need to activate visualization through clicking one of option in the left top selection box otherwise the boxplot will show review score distribution for all top product categories.

The fourth visualization shows how each seller performed in their corresponded top product category. It was obvious that customer satisfaction had positive relationship with delivery efficiency. From the box plot for each seller, no delay orders had high review score compared delay orders.

## Scatter plot and connected bar plot
![scatter_bar_plot](https://user-images.githubusercontent.com/68412645/145749337-931c4b12-61ee-4284-9be4-70861530bcb4.png)

Users could explore mean review score and mean delay time for delivery for top sellers corresponded to the top product category. When users move the mouse to click the scatter point, the corresponded delay time distribution for order delivery will be shown for a specific seller corresponded to the top product category.


The fifth visualization shows the specific relationship between delay time and review score. When delay time is negative, it means that an order arrived earlier. Future seller could learn top sellers’ delivery distribution through delivery delay time distribution.

# Reflection
In conclusion, there are many proposed ideas achieved. Although completed initial proposed visualizations could achieve better analysis performance, it was hard to implement them as they proposed in the proposal. Firstly, it was insignificant to look at product id instead product categories since product id did not give any useful information since dataset did not provide corresponded product name. Secondly, delivery efficiency could not consider the factor, delivery way. It was also not provided in dataset. Thirdly, initial proposed all connected visualizations could not be finished since I only know how to do it using dash. However, dash is based on server to update data when clicking one visualization to push other visualizations automatically do corresponded changes. I tried another way was used to connect different visualizations through designed selection boxes. Last, there were no time series visualization display as mentioned in the initial proposal. The reason was that there were no significant findings for time series data, and 2018 data was enough to provide significant findings compared to using 2016-2018 data. It was proved using simply time series plots before considering building a complex interactive visualization. Also, there were no period changes for data.

If I have an opportunity to start my project from scratch, I would combine other datasets to better define delivery efficiency and have a broader EDA steps for the whole dataset to understand dataset more efficiently before building any significant interactive visualizations to save much time
