""" 
    Takes urls for Lee County Shapefiles 
    Retrieves URLs (which are for ZIP files with GIS SHAPEFILE data)
    Stores URL download on system
    Unzips zipfile download and stores unzipped files on system
    Reads in shapefile data by taking <.SHP> file from unzipped dir  
    Stores shapefile data as JSON data for MySQL CRUD (e.g. INSERT/UPDATE) Operations
"""

##### links
# Parcel Shapefile:  https://www.arcgis.com/sharing/rest/content/items/d6c42c6e3268484a8512b7ec57ecdb2f/data
# Parcel-Points Shapefile:  https://www.arcgis.com/sharing/rest/content/items/3b1aca2b09884d4ca60a7eafc3cb1787/data


import fiona 
import json
import os 
import requests
import shapefile


