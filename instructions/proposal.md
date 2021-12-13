Over the rest of the semester, you will work towards creating an interactive data-driven story (narrative visualization)  based on the following requirements:

* You can use any publicly available dataset(s); however you may not use any of the following:
    * New York City Taxicab
    * Airline Delays
    * Amazon Reviews
    * Iris dataset
    * Penguins dataset
    * Any datasets used in labs or homework assignments
* If you use multiple datasets then you must be able to join or layer them in a way that makes sense. Pick something that interests you.
* Students may use the same dataset(s) with the condition that each student creates unique analysis and visualizations. This is individual work. If any visualization or narrative looks similar to that of another student that is using the same dataset, then **the grade will be split**. 
* Ideally, your dataset(s) will include:
    * Both qualitative and quantitative data
    * A time element
    * A geospatial element
    * A text element
    * The ability to be transformed into a graph
* Your narrative must include the following elements:
    * **At least 5** different views / visualization components (e.g. 3 bar charts only count as 1 component).
    * At least 1 of these views must be an "innovative view" that is either (a) an extension of an existing visualization type, or (b) a novel visualization type.
    * Multiple views coordinated with linked highlighting. A click/hover/selection interaction within one view must trigger a change in a different view. At least 2 views need to be linked. 
    * Include interactive tooltips, in at least one view, that are shown when users hover over marks.
* You don't necessarily need to show everything within a single-screen dashboard. You may want to use a tab navigation or a [scrollytelling](https://medium.com/nightingale/from-storytelling-to-scrollytelling-a-short-introduction-and-beyond-fbda32066964) approach.
* The interactive visual narrative will not include any server side or custom backends (Node.js, Python, etc) and database systems, such as Postgres or MySQL, although they could facilitate more powerful applications. In this project, your efforts will be purely on the data manipulation and presentation using front-end development (JavaScript, D3, HTML, CSS) and scripting languages R and Python (with appropriate packages that wrap D3 or its variants). 
* You can use CSS frameworks, such as [Bootstrap](https://getbootstrap.com/), [Materialize](https://materializecss.com/), or [Distill](https://distill.pub/about/) and include external libraries (jQuery, leaflet.js, moment.js, ...).  Layers such as NVD3, Vega-lite, Highcharts, etc. are allowed. Many of these have wrapper packages in R and Python. For example, the package `altair` (in both [R](https://vegawidget.github.io/altair/) and [Python](https://altair-viz.github.io)) wraps Vega-lite, and the package `plotly` (in both [R](https://plotly.com/r) and [Python](https://plotly.com/python)), among other packages, wraps D3. Other packages you may use are any of the [`htmlwidgets`](https://www.htmlwidgets.org) packages in R, [`bokeh`](https://bokeh.org) or [`holoviz`](https://holoviz.org) (and it's accompanying ecosystem) in Python, as well as specialized packages for geospatial ([`leaflet`](https://rstudio.github.io/leaflet/), [`tmap`](https://geocompr.robinlovelace.net/adv-map.html) in R, [`folium`](https://python-visualization.github.io/folium/index.html) in Python) and networks ([`igraph`](https://igraph.org), [`NetworkX`](https://networkx.org), `bokeh`, `plotly`). Any other packages you may use from R or Python or Javascript requires prior instructor approval. 
* You may choose to develop the whole narrative directly in D3 and JavaScript, however, in class we will be focusing on showing you R and Python wrappers to D3 and JavaScript that will make generating visualizations easier. 

The project will be evaluated using the following high-level criteria:

* Visual design: effectiveness of visualizations and interactions, which should link back to usage scenarios, tasks, and intended audience
* Level of technical difficulty and quality of implementation
* Whether the visual narrative answers a question, tells a story, and addresses the goals and requirements
* Quality and clarity of your writing and overall presentation, including your own visual style

## Proposal submission

**You will submit your project proposal as a single PDF, with the following sections in this order:**

1. Basic info
2. Overview
3. Description of the data
4. Usage scenario & tasks
5. Description of visualization & initial sketch
6. Work breakdown and schedule

Your proposal should be no more than 1,500 words of text (for context, this equates to a little over 1.5 pages of single-spaced Times New Roman size 11 text). You will also submit 1-5 sketches of your visual narrative, included in the same PDF (which should be no longer than 3 pages in total)

The first four sections of your proposal will be marked as a whole, and you will be assessed on the quality and clarity of your writing, the feasibility of what you propose, and your initial project description and sketch. The following sections are required

### Section 1: Basic info

- Project title

### Section 2: Overview

- A few sentences that describe what problem your visualization is tackling and how. You don't necessarily need to create a project that is purely focused on exploratory data analysis. You may choose to tell an interactive data-driven story intended to be consumed by the general public. The theme of your visualization can draw from any topic, including current affairs, history, natural disasters, and research findings from the sciences and humanities. State the intended audience. Be brief and clear.

For example:

>  Missed medical appointments cost the healthcare system a lot of money and affects the quality of care. If we could understand what factors lead to missed appointments it may be possible to reduce their frequency. To address this challenge, I propose building a data visualization that allows health care administrators to visually explore a dataset of missed appointments. My app will use show the distribution
> of factors contributing to appointment show/no show and allow users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to absence.

### Section 3: Description of the data and data preprocessing

You may use any publicly available dataset(s), except for 

* New York City Taxicab
* Airline Delays
* Amazon Reviews
* Iris dataset
* Penguins dataset
* Any datasets used in labs or homework assignments

In your report, briefly describe the dataset and the variables that you will visualize. All data has to be publicly available. *Provide a link to your data sources.*

Please note, if your dataset has a lot of variables and you plan to visualize them all, then provide a high level descriptor of the variable types, for example say the dataset contains demographic variables instead of describing every single variable. For example: 

> I will be visualizing a dataset of approximately 300,000 missed patient appointments. Each appointment has 15 associated variables that describe the patient who made the appointment (PatientID, Gender, Age), the health status of the patient (Hypertension, Diabetes, Alcohol intake, physical disabilities), information about the appointment itself (appointment ID, appointment date), whether the patient showed up (status), and if a text message was sent to the patient about the appointment (SMSsent). Using this data I will also derive a new variable, which is the predicted probability that a patient will show up for their appointment (ProbShow)

In the above example, specific variables names are indicated in the parenthesis; remember if your dataset has a lot of varibles stick to summaries and don't provide specific variable names. The example also differentiates variables that come with the dataset (i.e. Age) from new variables that you might derive for your visualizations (i.e ProbShow) - you should make a similar distinction in your write-up.

#### Preprocessing

Do you need to preprocess or clean up the original data? Do need to join multiple datasets? How do you plan to implement the processing pipeline? (R or Python scripts, or other means?)

### Section 4: Usage scenarios & tasks

The purpose of the usage scenario is to get you to think about how someone else might use the website you're going to design, and to think about those needs before you start hacking. Usage scenarios are typically written in a narrative style and include the specific context of usage, tasks associated with that
usage context, and a hypothetical walkthrough of how the user would accomplish those tasks with your visualization. If you are using a Kaggle dataset, you may use their "Overview (inspiration)" to create your usage scenario, or you may come up with your own inspiration.

Example usage scenario with tasks (tasks are indicated in brackets, i.e. [task])

> Mary is a policy maker with the Canadian Ministry of Health and she wants to understand what factors lead to missed appointments in order to devise an intervention that improves attendance numbers. She wants to be able to [explore] a dataset in order to [compare] the effect of different variables on absenteeism and [identify] the most relevant variables around which to frame her intervention policy.
> When Mary logs on to the "Missed Appointments app", she will see an overview of all the available variables in her dataset, according to the number of people that did or did not show up to their medical appointment. She can filter out variables for head-to-head comparisons, and/or rank order patients according to their predicted probability of missing an appointment. When she does so, Mary may notice
> that "physical disability" appears to be a strong predictor missing appointments, and in fact patients with a physical disability also have the largest number of missed appointments. She hypothesizes that patients with a physical disability could be having a hard time finding transportation to their appointments, and decides she needs to conduct a follow-on study since transportation information is not captured in her current dataset.

Note that in the above example, "physical disability" being an important variable is fictional - you don't need to conduct an analysis of your data to figure out what is important or not, you just need to imagine what someone could find, and how they may use this information.

### Section 5: Description of your visualization and sketch

Building from your usage scenario, give a high-level description of the visualization interface you will build. What are must-have features without which you would consider your project a failure? Remember to be realistic since you are actually required to implement this interactive visualization, and you will be assessed on
how much, and why, your finalproject deviates from this initial proposal.


Briefly describe the characteristics of your "innovative view component" that is either an extension of an existing visualization type or a novel visualization type. What makes it special?


Your sketch can be hand-drawn or mocked up using Powerpoint, a graphics editor, or wireframe tools, such as Balsamiq. Most likely, you will need more than one image to show your proposed visual design and interaction sequences. Don't use more than five sketches. Please note, this is a very basic illustrative guide that should help you during the implementation of the first prototype. It is by no means the limit of what you should submit as the final project.

### Section 6: Work breakdown and schedule

Include a list of project milestones, breaking down the work into a series of smaller chunks that are meaningful and useful for your specific project. Your milestone list shouldn't just be completely generic (eg "requirements analysis, design, initial coding, iterative refinement, final writeup"). While something analagous to these stages may well make sense for your project, you should also be thinking about how to break down the work into components that are appropriate for your project in specific (eg "create initial static version of view X", "link views X and Y to each other"). As above, think about these questions: What are must-have features? What are optional features that can be implemented after the second milestone, if there is time? Milestones must be associated with two numbers: the estimate of the number of hours each chunk of work will take, and the target date for completion of that chunk. 
The scope of the work should be roughly 50-75 hours for the entire project -- across all three milestones.
