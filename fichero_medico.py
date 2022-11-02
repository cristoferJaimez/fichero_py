# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:50:35 2022

@author: cjaimez
"""

import pandas as pd

from function.readFiles import ReadingFiles
from function.listFolder import ListenDir
from function.cleanTxt import Clean
from function.crossing_one_ import Crossing


#activa menu
url = ListenDir().listenDir()
#leer archivo seleccionado
res = ReadingFiles.reading('', url)


#limpiar direcciones
name_clean = Clean.clean_name(res[1])
adress_clean = Clean.clean_adress(res[1])


print(name_clean)
#print(adress_clean)
#print(res[0])
#print(res[1])
#setData = Crossing.crossing_one(res[0], res[1])
#print(setData)


