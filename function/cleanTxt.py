# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:18:29 2022

@author: cjaimez
"""


from contexto.limpieza import limpieza_texto

class Clean:
    
        
    
    #LIMPIAR NOMBRES
    def clean_name(data):
        column_name = []
        print('Cleaning names...')
        for i in range(len(data)):
            name = limpieza_texto(data['NOMBRE DEL MEDICO'].iloc[i] , 
                                  quitar_numeros=True, 
                                  quitar_acentos=True,
                                  momento_stopwords="ñ"
                                 )
            #print(name.upper())
            column_name.append(name.upper()) 
        return column_name   
        
        
        
        
    #LIMPIAR DIRECCIONES
    def clean_adress(data):
        column_adress = []
        print('Cleaning adress...')
        for i in range(len(data)):
            txt = data['Dirección'].iloc[i]    
            idx = txt.find("#")
            
            try:
                if idx > 0:
                    adress = limpieza_texto(data['Dirección'].iloc[i], 
                                          quitar_numeros=False, 
                                          quitar_acentos=True,
                                          momento_stopwords="####"
                                         )
               
                    stra = adress[:idx] + '#' + adress[idx:]
                    column_adress.append(stra.upper()) 
                else:
                    column_adress.append(adress.upper())
                   
            except Exception as e:
                print(e)
                pass
        return column_adress
            
     
     




