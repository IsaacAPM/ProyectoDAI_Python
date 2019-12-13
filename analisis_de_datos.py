#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:16:25 2019

@author: ipiment
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
#En esta celda se lee el archivo de crimenes y se gurada en max_crime los datos de los 
#tres paises con mas crimen
crimes = pd.read_csv("SYB62_328_201904_Intentional Homicides and Other Crimes.csv")
max_crime = pd.DataFrame()
max_crime["Value"] = crimes["Value"].nlargest(3)
max_crime = pd.merge(max_crime,crimes,on="Value")
print(max_crime["Intentional homicides and other crimes"])
#%%
