# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:58:23 2022

@author: cjaimez
"""

import pandas as pd
from tqdm import tqdm
import os

class City:
    
    def city(data, zi):
        print('Searchs Cities...')
        column_region = []
        cod = ""
        
        for i in  tqdm(range(len(data))):
            ciudad = (data['Ciudad'].iloc[i])
            region_ = (data['REG'].iloc[i])
            for x in range(len(zi)):
                res =   ciudad in zi['Unnamed: 3'].iloc[x] 
                #reg =   region_ in zi['SIGLA REG'].iloc[x]
                if res == True:
                    #print(zi['REGION'].iloc[x], ' in  ' , ciudad, ' =', res)
                    cod = zi['Unnamed: 4'].iloc[x]
                    break
                else:
                    cod = 'Null'
        
                    
            column_region.append(cod)
                    
                
        
        #buscar ciudad
        #City.search_code_cite(column_region)   
        
        return(column_region)
