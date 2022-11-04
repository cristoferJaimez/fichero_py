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
        print('Reading DB_COLOMBIA_PANEL plase wait...')
        db_panel = pd.read_excel('./db/1 - Recibidos Consolidado 1101_2022  (3) (1).xlsm', sheet_name='4-Zonas de influencia')
        
        return [db, file, zi, db_panel]
