import pandas as pd
from tqdm import tqdm

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
def search(data, db):    
    acum = []
    for i in tqdm(range(len(data))):
        medic = str(other_df['CIUDAD_MEDICO'].iloc[i])
        
        for x in range(len(db)):
            db_medic = str(db['Codigo de Ciudad & Nombre delMedico Arreglado'].iloc[x])
            
            #comparacion 
            dif = DiferenciaStrings().comparacion_lista(medic,db_medic, tipo='jaro_winkler', norm=None)
            if dif[0] > 0.9:
                resp = [
                        medic,
                        db['COD CIUDAD'].iloc[x],
                        db['Nombre del Medico arreglado'].iloc[x],
                        db['ESPECIALID COMPLETA'].iloc[x],
                        dif[0]
                             ]  
                acum.append(resp)
    return acum            
  
da = search(other_df, db_)
    
df_ = pd.DataFrame(da)
print('save')
conc.to_csv('resultado_cruze.csv', header=True, index=False, sep="|")  
df_.to_csv('zonas de influencia.csv', header=True, index=False, sep="|")  

print('end')     