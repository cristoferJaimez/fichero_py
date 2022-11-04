import pandas as pd
from tqdm import tqdm
import threading
import numpy as np
import numba as nb

from contexto.comparacion import Similitud, Distancia, DiferenciaStrings

print('Reading DB_COLOMBIA plase wait...')
db_ = pd.read_excel('./db_panel/1 - Recibidos Consolidado 1101_2022  (3) (1).xlsm', sheet_name='COLOMBIA-2020 septiembre')
print('Reading archivo plase wait...')
file = pd.read_excel('./db_panel/COPSERVIR - OCTUBRE 2022 - CADENA DE DROGUERIAS.xlsx')   

print('searchs...')
join = file.merge(db_, how='left', left_on='CIUDAD_MEDICO',right_on='Codigo de Ciudad & Nombre delMedico Arreglado',suffixes=('_left', '_right'))
ex = join[[ 'COD CIUDAD', 'Nombre del Medico arreglado', 'ESPECIALID COMPLETA']]
print('proccesing')
df = pd.DataFrame(ex)
#ok = medic(db_, file)
conc = pd.concat([file, ex], axis=1)

#eliminar colunas vacias
conc.dropna(how='all', axis=1, inplace=True)

print('any...')
other_df = conc[conc['Nombre del Medico arreglado'].isnull()]


#recorrer faltantes
"https://ucd-dnp.github.io/ConTexto/versiones/master/ejemplos/01_lectura_y_escritura_de_documentos.html#lectura-y-escritura-de-documentos"
def search(data, db, init, limit):    
    acum = []
    for i in range(init ,limit):
        medic = str(other_df['CIUDAD_MEDICO'].iloc[i])
        
        for x in range(len(db)):
            db_medic = str(db['Codigo de Ciudad & Nombre delMedico Arreglado'].iloc[x])
            
            #comparacion 
            dif = DiferenciaStrings().comparacion_lista(medic,db_medic, tipo='jaro_winkler', norm=None)
           
            if dif[0] > 0.87:
                print('item:  #',i,' |',"\n NAME: |", medic, ' |SEARCH: ', db_medic, ' | %', dif[0][0]*100)
                resp = [
                        medic,
                        db['COD CIUDAD'].iloc[x],
                        db['Nombre del Medico arreglado'].iloc[x],
                        db['ESPECIALID COMPLETA'].iloc[x],
                        dif[0][0]
                             ]  
                acum.append(resp)
                
    return acum            
hilo1 = threading.Thread(target=search(other_df, db_, 0, 5000))
hilo2 = threading.Thread(target=search(other_df, db_, 5000, 10000))
hilo3 = threading.Thread(target=search(other_df, db_, 10000, 15252))
print('init hilo one')
hilo1.start()
print('init hilo two')
hilo2.start()  
print('init hilo three')
hilo3.start()  
#da = search(other_df, db_)

df_hilo_1 = pd.DataFrame(hilo1)
df_hilo_2 = pd.DataFrame(hilo2)
df_hilo_3 = pd.DataFrame(hilo3)
    
df_search = pd.concat([df_hilo_1,df_hilo_2,df_hilo_3])

#df_ = pd.DataFrame(da, columns=['CIUDAD_MEDICO','COD CIUDAD','Nombre del Medico arreglado','ESPECIALID COMPLETA', '%'])
print('save')
conc.to_csv('resultado_cruze.csv', header=True, index=False, sep="|")  
df_search.to_csv('zonas de influencia.csv', header=True, index=False, sep="|")  

print('end') 
