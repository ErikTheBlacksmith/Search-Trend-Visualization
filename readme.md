# Search Trend Visualization
![image of the application](https://i.imgur.com/hgSJ5HM.png)

do not steal please i made this :)

How to use:
Run app.R
Fill out boxes
Click "Apply Changes"


How it works:
Since pytrends can take a maximum of 5 inputs as once, the code uses the first term as a pivot to normalize the rest of the data in groups of 4


R and python required
Uses R packages shiny, ggplot2, and reticulate
Uses Python packages pytrends and pandas (dependancy of pytrends)


Tips:
If parts of the data are missing, try making the first term the most popular

Sometimes it likes to close so just reopen it

If you get a substring error, try making a graph with a single search term, that usually fixes the problem

If you get a request error, go to https://trends.google.com and make a request, then restart the app