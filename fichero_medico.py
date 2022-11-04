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
from function.city import City
from function.medic import Medic


#activa menu
url = ListenDir().listenDir()
#leer archivo seleccionado
res = ReadingFiles.reading('', url)


#limpiar nombre y direcciones
name_clean = Clean.clean_name(res[1])
adress_clean = Clean.clean_adress(res[1])

#buscar codigo ciudad
code_city = City.city(res[1],res[3])

#BUSCAR MEDICO EN BASE DE DATOS COLOMBIA
medic = Medic.medic(res[0], res[1], code_city)
