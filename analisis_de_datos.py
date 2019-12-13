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
crimes = pd.read_csv("./Datos/SYB62_328_201904_Intentional Homicides and Other Crimes.csv")
max_crime = pd.DataFrame()
max_crime["Value"] = crimes["Value"].nlargest(3)
max_crime = pd.merge(max_crime,crimes,on="Value")
max_crime.to_csv("./Datos_filtrados/Los 3 países con mayor indice de criminalidad.csv")
name_crime = max_crime["Intentional homicides and other crimes"]
#%%
#En esta celda se grafica los datos optenidos en la anterior
fig, axes = plt.subplots()
axes.bar(name_crime,max_crime["Value"])
axes.set_title("Paises con mayor índice de criminalidad")
axes.set_xlabel("País")
axes.set_ylabel("Índice de criminalidad")
fig.savefig("./Gráficas/países_mayor_indice_crimenes.pdf")
#%%
#En esta celda leemos los datos de los dos archivos restantes a analizar
#el primero es el GNI per capita y el segundo el ratio de inscripción a escuelas secundarios 
GNI_per_capita = pd.read_csv("./Datos/GNI_per_capita.csv")
Gross_enrolment_ratio_Secondary_education = pd.read_csv("./Datos/Gross_enrolment_ratio_Secondary_education.csv")
#%%
#En esta celda se extraen los datos de los paises obtenidos en la primera celda de la tabla GNI per capita 
GNI_crime = GNI_per_capita[(GNI_per_capita["Country or Area"] == name_crime[0]) | (GNI_per_capita["Country or Area"] == name_crime[1]) | (GNI_per_capita["Country or Area"] == name_crime[2])]
GNI_crime.to_csv("./Datos_filtrados/GNI per capita de los 3 países con mas crimen.csv")
#%%
#En esta celda se extraen los datos de los paises obtenidos en la primera celda de la tabla Gross enrolment ratio secondary education
Secondary_crime = Gross_enrolment_ratio_Secondary_education[(Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime[0]) | (Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime[1]) | (Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime[2])]
Secondary_crime.to_csv("./Datos_filtrados/Ratio de inscripción a secundaria de los 3 países con mayor criminalidad.csv")
#%%
fig, axes = plt.subplots(figsize=(30,6))
GNI_crime_0 = GNI_crime[GNI_crime["Country or Area"] == name_crime[0]].sort_values(by='Year', ascending=True)
GNI_crime_1 = GNI_crime[GNI_crime["Country or Area"] == name_crime[1]].sort_values(by='Year', ascending=True)
GNI_crime_2 = GNI_crime[GNI_crime["Country or Area"] == name_crime[2]].sort_values(by='Year', ascending=True)
axes.plot(GNI_crime_0["Year"], GNI_crime_0["Value"],"bo-",label=name_crime[0])
axes.plot(GNI_crime_1["Year"], GNI_crime_1["Value"],"ro-",label=name_crime[1])
axes.plot(GNI_crime_2["Year"], GNI_crime_2["Value"],"go-",label=name_crime[2])
axes.set_title("Variación del GNI per capita de los 3 países con mayor índice de criminalidad")
axes.set_xlabel("Año")
axes.set_ylabel("GNI per capita")
axes.legend(loc="upper left")
fig.savefig("./Gráficas/Variación del GNI per capita de los 3 países con mayor índice de criminalidad.pdf")
#%%
