# Crop detection
This repository contains the files needed to create a web application for detecting illegal crops, the first page is used to search or pick an image, the second one is for statistics. This app is still work in progress.

The main file is located in the main folder, called app.py, this file calls the other files located in the **pages** folder to render the body of the app, overview and statistics. 

The **assets** folder has support files like css and png (images) for the styling of the webpage.

The **data** folder contains a csv file which contains a dummy dataset to populate the table in the statistics page, since this app was adapted from <a href=https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-financial-report> Dash Financial Report</a>.

Finally in the **main** folder, besides the main app there are other supporting files like the models used to predict if the images has illegal crops or not.
