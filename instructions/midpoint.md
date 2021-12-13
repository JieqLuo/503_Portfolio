# Mid-point Project Submission

Review the [proposal](proposal.md) requirements.

## Submission

* Tag a release of your project with tag version `v0.1-wip` by the **due date**. Tagging a release allows you to continue the development, even before the mid-point is graded. [See instructions for creating releases on Github](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) (This is in line with professional standards when using git). Your release must contain your first prototype implementation and a README.md with your writeup. 

* Push your code to [GitHub](www.github.com)

* In addition to pushing your repository to GitHub, you will need to submit on [Canvas](georgetown.instructure.com) as well:
	* Please create a single `zip` file of the entire directory by right-clicking on the directory name and creating a zip file from it (depending on your OS.) 
	* The `zip` file name should be named `midpoint-firstname-lastname.zip` 

* Edit the `README.md` file as your mid-point writeup (see writeup section below)


## Implementation

* Turn your project proposal into an interactive web-based visualization using the tools you learned in class:
    - R and all of the packages
    - Python and all of the packages
    - d3

* Your interactive web-based visualization should be accessible via an `index.html` file in the root level of your repository. You can choose however you would like to build your website (using `Rmarkdown`, editing HTML directly, etc.)

* Make sure that your code is well-organized and easy to read. Use separate files for visualization components, use functions to promote code reuse. Don't work with a messy repo and then try to clean it up before the final milestone. Comment your code early on! 

* Read the [repository-structure.md]() description of the repository structure

* Implement the features you outlined in your proposal. You don't need to have all details fully implemented but the general user interface and all views (visualization components) must exist. Don't worry about missing tooltips or small usability issues.

* Your interface should be as self-documenting as possible, with appropriate labels for panes, axes, and widgets, a legend documenting the meaning of visual encodings, and a meaningful title and description for the project.
  
* Keep your usage scenario (from your proposal) in mind when designing your interface. Make sure that your visualization's interface and functionality either:
  + allows a user to answer your proposed question, or 

  *  successfully communicates a message or series of messages (narrative visualization).

* It can be easy to get sucked into a rabbit hole when trying to implement a stubborn feature. While it is important to build skills troubleshooting, we do not want one feature to prevent you from completing the full first prototype. If you're stuggling with a particularly tough problem, some ideas are: 

    > save it for later, or discuss with the instructional team!

### Reminders

* The interactive visual narrative will not include any server side or custom backends (Node.js, Python, etc) and database systems, such as Postgres or MySQL, although they could facilitate more powerful applications. In this project, your efforts will be purely on the data manipulation and presentation using front-end development (JavaScript, D3, HTML, CSS) and scripting languages R and Python (with appropriate packages that wrap D3 or its variants). 

* You can use CSS frameworks, such as [Bootstrap](https://getbootstrap.com/), [Materialize](https://materializecss.com/), or [Distill](https://distill.pub/about/) and include external libraries (jQuery, leaflet.js, moment.js, ...).  Layers such as NVD3, Vega-lite, Highcharts, etc. are allowed. Many of these have wrapper packages in R and Python. For example, the package `altair` (in both [R](https://vegawidget.github.io/altair/) and [Python](https://altair-viz.github.io)) wraps Vega-lite, and the package `plotly` (in both [R](https://plotly.com/r) and [Python](https://plotly.com/python)), among other packages, wraps D3. Other packages you may use are any of the [`htmlwidgets`](https://www.htmlwidgets.org) packages in R, [`bokeh`](https://bokeh.org) or [`holoviz`](https://holoviz.org) (and it's accompanying ecosystem) in Python, as well as specialized packages for geospatial ([`leaflet`](https://rstudio.github.io/leaflet/), [`tmap`](https://geocompr.robinlovelace.net/adv-map.html) in R, [`folium`](https://python-visualization.github.io/folium/index.html) in Python) and networks ([`igraph`](https://igraph.org), [`NetworkX`](https://networkx.org), `bokeh`, `plotly`). Any other packages you may use from R or Python or Javascript requires prior instructor approval. 

* You may choose to develop the whole narrative directly in D3 and JavaScript, however, in class we will be focusing on showing you R and Python wrappers to D3 and JavaScript that will make generating visualizations easier. 


## Write-up

In addition to the implementation, you must document the functionality of your visualization project in a markdown document `README.md` in the root directory of your git repository.

* Your writeup should include the rationale for your design choices, focusing on the interaction aspects and connecting these choices to a data abstraction (including a characterization of the raw data types and their scale/cardinality, and of any derived data that you decided to compute) and the task abstraction. You should also concisely describe your visual encoding choices.

* Talk about how your vision has changed since your proposal
     * How have your visualization goals changed?
    * Does your visualization enable the tasks you set out to facilitate or successfully communicate the story you want to tell?

* Add at least one screenshot to your document that illustrates your current prototype. Make sure that all of the views you have implemented so far are documented in screenshots, you may need more than one.

* **Add a link to the original data source(s).**

* Briefly describe your current data preprocessing pipeline, if there is one.