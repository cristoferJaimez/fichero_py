# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:01:58 2022

@author: cjaimez
"""

import pandas as pd


class ReadingFiles:
    
    def reading(self, route):
        print('Reading plase wait...')
        db = pd.read_excel('./db/COLOMBIASEP22.xlsx')
        file = pd.read_excel(route)
        return [db, file]
