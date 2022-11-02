# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:58:23 2022

@author: cjaimez
"""

import pandas as pd


class City:
    
    def city(data, zi):
        print('Concatenated Cities...')
        for i in range(len(data)):
            region = (data['Distrito 2'].iloc[i]).split()
            print(region[1])