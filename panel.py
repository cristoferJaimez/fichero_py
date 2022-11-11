import pandas as pd
from tqdm import tqdm
import threading

import math

from concurrent.futures  import ThreadPoolExecutor 

from contexto.comparacion import DiferenciaStrings

import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

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

acum = []

executer = ThreadPoolExecutor(max_workers=10)

def search(data, db, init, limit):    
    
    logging.info(f'Task start: init {init} end {limit}!!\n') 
   
    for i in range(init ,limit):
        medic = str(other_df['CIUDAD_MEDICO'].iloc[i])
        
        for x in range(len(db)):
            db_medic = str(db['Codigo de Ciudad & Nombre delMedico Arreglado'].iloc[x])
            #comparacion 
            dif = DiferenciaStrings().comparacion_lista(medic,db_medic, tipo='jaro_winkler', norm=None)
           
            if dif[0] > 0.87:
                logging.info(f'|item:{i}/{limit}| medic: {medic}  |medic DB: {db_medic} |{round(dif[0][0]*100)}%|\n') 
               
                #print('hilo: ', threading.current_thread().getName() ,  ' item:  #',i,' |',"\n NAME: |", medic, ' |SEARCH: ', db_medic, ' | %', dif[0][0]*100)
                resp = [
                        medic,
                        db['COD CIUDAD'].iloc[x],
                        db['Nombre del Medico arreglado'].iloc[x],
                        db['ESPECIALID COMPLETA'].iloc[x],
                        dif[0][0]
                             ]  
                acum.append(resp)
    
    logging.info(f'Task end: init {init} end {limit}!!\n')            
    return acum       



def createHilo(data): 
    num_int = len(data) / 10
    print( math.ceil(num_int))
    var_ini = 0
    rangeCol = math.ceil(num_int)
    var_fin = math.ceil(num_int)
    #var_dim = []
    
    """
    for j in range(1,12):
        var_dim.append('hilo'+str(j))
    """
    
    
    for i in range(1, 11):
        if str(i) == '1':
            var_ini = 0
        else:    
            var_ini = var_fin
        
        var_fin = rangeCol * i
        executer.submit(search,other_df, db_, var_ini, var_fin)
        var_ini = var_fin    
        
     
    
    """
    for k in range(1,12):
        var_dim[k].join()
    """    
       
    
    
    

createHilo(other_df)

#da = search(other_df, db_)






df_acum = pd.DataFrame(acum, columns=['In nomnre medico', 'out UTC', 'out Medico ', 'out Espec', 'out %'])

#df_ = pd.DataFrame(da, columns=['CIUDAD_MEDICO','COD CIUDAD','Nombre del Medico arreglado','ESPECIALID COMPLETA', '%'])
print('save')
conc.to_csv('resultado_cruze.csv', header=True, index=False, sep="|")  
df_acum.to_csv('zonas de influencia.csv', header=True, index=False, sep="|")  

print('end') 
