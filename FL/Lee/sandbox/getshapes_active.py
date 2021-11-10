''' Take data from shapefiles and prep for pandas ''' 

from pathlib import Path
import fiona
import fnmatch
import json
import os
import pandas as pd
import re
import shapefile


## go to folder where .SHP file was unzipped 

"""
def fileFinder(root, patterns='*', rcurse=1, return_folders=0):
    # delimit semicolon delimited (;) pattern string 
    patternList = patterns.split(";")

    # collect input/output args into single bunch
    class Bunch:
        def __init__(self, **kwargs): 
            self.__dict__.update(kwargs)

    currentBunch = Bunch(rcurse=rcurse, 
            patternList=patternList,
            return_folders=return_folders,
            hits=[])

    def scan(currentBunch, dirname, files):
        # append currentBunch.hits 
        for fname in files:
            abspth = os.path.normpath(os.path.join(dirname, fname))

            if currentBunch.return_folders or os.path.isfile(abspth):
                for pattern in currentBunch.patternList:
                    if fnmatch.fnmatch(fname, pattern):
                        currentBunch.hits.append(abspth)
                        break
            
        # block recursion if recursion disallowed (e.g. permission error)
        if not currentBunch.rcurse:
            files[:] = []       ## pretend its empty to move to next recursion element

    os.walk(root, scan, currentBunch)
    return currentBunch.hits
"""

dwnlnds_abspath = "/home/csorndog/code/projects/python/lifetimeprop/datasourcing/scrapeGisData/FL/Lee/sandbox/downloads"
print("Testing fileFinder (shapefile finder)")


# test funct
#fileFinder(dwnlnds_abspath,'*.shp')
#print(fileFinder(dwnlnds_abspath))




# easier version
def search_tree(root=None,pattern=None):
    """ return all contents for "pattern=None" """
    def setroot(rootdir=None):
        if not rootdir:
             rootdir = os.getcwd()
        return rootdir

    def pattern_input_check():
        if not pattern:
            pattern = str(pattern)
        return pattern

    # traverse dir and subdirs
    search_matches = []
    for root, dirs, files in os.walk(setroot(root)):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for f in files:
            if not pattern:
                pattern = "*"
            if re.search(pattern,f):
                print(f)
                search_matches.append(f)

    return search_matches


print("Search Tree test")
print(search_tree(dwnlnds_abspath,".shp$"))
