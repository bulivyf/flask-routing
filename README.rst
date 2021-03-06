README
FLASK GEOSPATIAL example

README
Author: Evan Fraser


INTRODUCTION
The code uses OpenLayer to present a map of the area west of DC that calculates geospatial distance between points. To do this, the user should click multiple consecutive points to set (lat,lon) positions on the map. Once a double click is made the application gathers all the points and calculates geospatial distances between each. The (lat,lon) and distances between each are presented below the map as html tables after the double click event.

SERVER CALCULATION
The Flask web server does rudimentary nearest neighbor calcs from the json coords and distances.  From there a number of 'closest' lines are calculated; all based on line-of-sight as viewed from the visible map.
Then kml is generated and pushed to the client.  The client renders the kml.

TODO
Though the respective steps are in place, some details still need ironed out.  For example OpenLayer doesnt seem to easily accommodate POST sending JSON from the client and then the response being pure kml.


DEVELOPER NOTES

Python version: Anaconda 3

IDE: PyCharm Community Edition 2018.2 (for personal use only)

This is a Flask (server based) version of the "Routing" project also on github.  Initial tests in generating kruskal networks with Javascript showed it wasn't ideal for the task (working with and copying matrices resulted in slow performance).  So this version starts with that initial code, but will remove it in favor of a python implementation which will be called via REST.


To run the web server application type (in the anaconda (commandline) prompt):

    ```python runner.py runserver```

then navigate to the url that the console lists.  It's likely http://localhost:5000 or very similar.  Use the map as described in the INTRODUCTION section.
FYI: This is a prototype, so the calculated lines are still work in progress.

REFERENCE
OpenLayers
https://openlayers.org/en/latest/examples/
Look at web/templates/index.html for current version.
Last check: v4.6.5

Stamen Maps
http://maps.stamen.com/

