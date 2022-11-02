# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:58:23 2022

@author: cjaimez
"""

import pandas as pd


class City:
    
    def city(data, zi):
        print('Concatenated Cities...')
        column_region = []
        for i in range(len(data)):
           region = (data['Distrito'].iloc[i]).split()
           region = region[1]
           column_region.append(region[:2])
        
        #buscar ciudad
        City.search_code_cite(column_region)   
        return(column_region)
    
    
    def search_code_cite(data):
        print(data)