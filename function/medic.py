# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:10:35 2022

@author: cjaimez
"""

from tqdm import tqdm
import pandas as pd
from contexto.comparacion import  DiferenciaStrings
class Medic:
    
    def medic(db, data, cod_city):
        print("Search Medic to Data Base Colombia...")
        medic_res = []
        resp = ""
        

        #1 busquedad 100% de coincidencia
        #df
        df_db = pd.DataFrame(db)
        df_data = pd.DataFrame(data)
        df_cod_ciu = pd.DataFrame(cod_city)
        
        #res1 =  df_data.merge( df_db, how='left', left_index='', right_index='')
        
        for i in tqdm(range(len(data))):
            medic = str(cod_city[i])+str(data['NOMBRE DEL MEDICO'].iloc[i])
            acum = []
            for x in range(len(db)):
                
              db_medic = str(db['Codigo de Ciudad & Nombre delMedico Arreglado'].iloc[x])
              dif = DiferenciaStrings().comparacion_lista(medic,db_medic, tipo='jaro_winkler', norm=None)
              #print(medic , ' ', db_medic, ' ', dif[0])
              
              if dif[0] > 0.9:
                 resp = [
                         medic,
                         db['Codigo de Ciudad'].iloc[x],
                         db['Codigo de Ciudad & Nombre del Medico'].iloc[x], 
                         db['Codigo de Ciudad & Nombre delMedico Arreglado'].iloc[x],
                         db['Nombre del Medico'].iloc[x],
                         db['Nombre del Medico arreglado'].iloc[x],
                         dif[0]
                         ]
                 
                 acum.append(resp)
              
              #resultados mas altos
            if len(acum) > 0:
                    meidic,cod ,cod_med_ciud, cod_med_ciud_arr, nom_medic, nom_medic_arr, porc= max(acum, key=lambda item: item[6])
                    #print("\n",medic ,"  ",max_value, " ", nom___)
                    medic_res.append([meidic,cod, cod_med_ciud, cod_med_ciud_arr, nom_medic, nom_medic_arr, porc[0]])
            else:
                medic_res.append([meidic, 'Null', 'Null', 'Null', 'Null', 'Null', 'Null'])
    
                
         
        df = pd.DataFrame(medic_res)
        df.to_csv('busquedad.csv', header=True, index=False, sep="|")        
        return medic_res
            