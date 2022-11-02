# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:08:57 2022

@author: cjaimez
"""
import pandas as pd
from contexto.comparacion import Similitud, Distancia, DiferenciaStrings
from contexto.limpieza import *


class Crossing:
    
    
    def crossing_one(db,data):
        print('Crossing please wait...')
        #Crossing.crossing_city_code()
        for i in range(len(data)):
            #print(data.iloc[i]['NOMBRE DEL MEDICO'])
            str_1 = data.iloc[i]['NOMBRE DEL MEDICO']
            str_2 = data.iloc[i]['GERENTE']
            
            str_1 = limpieza_basica(str_1)
            str_2 = limpieza_basica(str_2)
            
            
            
            data_0 =  DiferenciaStrings().comparacion_lista(str_1, str_2, tipo='damerau_levenshtein', norm=None)
            data_1 =  DiferenciaStrings().comparacion_lista(str_1, str_2, tipo='levenshtein', norm=None)
            data_2 =  DiferenciaStrings().comparacion_lista(str_1, str_2, tipo='hamming', norm=None)
            data_3 =  DiferenciaStrings().comparacion_lista(str_1, str_2, tipo='jaro_winkler', norm=None)
            data_4 =  DiferenciaStrings().comparacion_lista(str_1, str_2, tipo='jaro', norm=None)
            print('damerau_levenshtein', data_0)
            print('levenshtein',data_1)
            print('hamming',data_2)
            print('jaro_winkler',data_3)
            print('jaro',data_4)

        
        return data
    
    
    
    #organizar codigo ciudad
    def crossing_city_code(data):
        return ''
        