#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado en diciembre 13 14:52:10 2019

@author: linces
"""
#IMPORTANTE: ESTE ARCHIVO SOLO FUE USADO UNA VEZ PARA LIMPIAR LOS DATOS DEL ARCHIVO CON LOS DATOS DE 
#CRIMINALIDAD CON EL FIN DE QUITAR LAS FILAS CON VALOR 0 YA QUE ESO IMPLICA QUE NO HAY DATOS DISPONIBLES 

import pandas as pd
import numpy as np

crimes = pd.read_csv("./Datos/SYB62_328_201904_Intentional Homicides and Other Crimes.csv")
index_drop = crimes[crimes["Value"] == 0].index
crimes.drop(index_drop,inplace = True)
crimes.to_csv("./Datos/SYB62_328_201904_Intentional Homicides and Other Crimes.csv")