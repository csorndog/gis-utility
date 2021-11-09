"""ts 
    Takes urls for Lee County Shapefiles 
    Retrieves URLs (which are for ZIP files with GIS SHAPEFILE data)
    Stores URL download on system
    Unzips zipfile download and stores unzipped files on system
    Reads in shapefile data by taking <.SHP> file from unzipped dir  
    Stores shapefile data as JSON data for MySQL CRUD (e.g. INSERT/UPDATE) Operations
"""

from datetime import datetime
from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile
import fiona 
import json
import os 
import requests
import shapefile


##### links
# Parcel Shapefile:  https://www.arcgis.com/sharing/rest/content/items/d6c42c6e3268484a8512b7ec57ecdb2f/data
parcels_url = "https://www.arcgis.com/sharing/rest/content/items/d6c42c6e3268484a8512b7ec57ecdb2f/data"
# Parcel-Points Shapefile:  https://www.arcgis.com/sharing/rest/content/items/3b1aca2b09884d4ca60a7eafc3cb1787/data
parcel_points_url = "https://www.arcgis.com/sharing/rest/content/items/3b1aca2b09884d4ca60a7eafc3cb1787/data"



def ttest(*urls):
    cwd = os.getcwd()
    abspth = os.path.join(cwd,'downloads')
    datestamp, timestamp = str(datetime.now()).split()
    print(abspth)

    for num,url in enumerate(urls,1):
        # var with zip download
        temppath = f"{abspth}"
        postfix = f"set.{num}" 
        fullpth = os.path.join(abspth,datestamp,postfix)
        print("")
        os.makedirs(fullpth, exist_ok=True)
        print(f"Created: {fullpth}")
        print("---------------------------------------------------------------------------------------------------")
        print("NEW DIRECTORY:  ")
        os.chdir(fullpth)
        print(f"\nCurrent Directory:  {os.getcwd()}")
    return
"""

        # download zip data to hard drive
        z = requests.get(url)
        with open(fullpth,'wb') as fz:
            with requests.get(url,stream=True):
                for chunk in z.iter_content(chunk_size=128):
                    fz.write(chunk)

"""
        
       # zdwnld = requests.get(url)
        #with open(f'download-0{num}','wb') as fd:
         #   with requests.get(url,stream=True) as rq:
          #      for chunk in rq.iterm_content(chunk_size=128):

        

        #        with open NamedTemporaryFile(

t2 = ttest(parcels_url,parcel_points_url)
print(t2)
