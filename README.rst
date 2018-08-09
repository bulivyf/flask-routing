README
FLASK GEOSPATIAL example

README
Author: Evan Fraser


INTRODUCTION
The code uses OpenLayer to present a map of the area west of DC that calculates geospatial distance between points. To do this, the user should click multiple consecutive points to set (lat,lon) positions on the map. Once a double click is made the application gathers all the points and calculates geospatial distances between each. The (lat,lon) and distances between each are presented below the map as html tables after the double click event.


OBJECTIVE
The initial objective is to present a baseline for implementing nearest neighbor.  All based on line-of-sight as viewed from the visible map.


DEVELOPER NOTES
Python version: Anaconda 3
IDE: PyCharm Community Edition 2018.2 (for personal use only)
This is a Flask (server based) version of the "Routing" project also on github.  Initial tests in generating kruskal networks with Javascript showed it wasn't ideal for the task (working with metrices and copying such slowed it all down).  So this version starts with that initial code, but will remove it in favor of a python implementation which will be called via REST.


To run the web server application type:

    ```python runner.py runserver```

then navigate to the url that the console lists.  Its likely http://loclahost:5000 or very similar.  Use the map as described in the INTRODUCTION section.


REFERENCE
OpenLayers
https://openlayers.org/en/latest/examples/


Stamen Maps
http://maps.stamen.com/

