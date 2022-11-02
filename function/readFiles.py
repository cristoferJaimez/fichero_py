# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:01:58 2022

@author: cjaimez
"""

import pandas as pd


class ReadingFiles:
    
    def reading(self, route):
        print('Reading plase wait...')
        print('Reading DB_COLOMBIA plase wait...')
        db = pd.read_excel('./db/COLOMBIASEP22.xlsx')
        print('Reading ZI_COLOMBIA plase wait...')
        zi = pd.read_excel('./db/COL_Zinfluencia_03082022.xlsx')
        print('Reading '+ route +' plase wait...')
        file = pd.read_excel(route, sheet_name='BASE')
        return [db, file, zi]
