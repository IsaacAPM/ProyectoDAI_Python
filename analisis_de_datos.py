#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado en diciembre 10 15:16:25 2019

@author: linces 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
#En esta celda se lee el archivo de crimenes y se gurada en max_crime los datos de los 
#tres paises con mas crimen
crimes = pd.read_csv("./Datos/SYB62_328_201904_Intentional Homicides and Other Crimes.csv")
#En la siguiente instrucción filtramos los datos obtenidos para solo tomar los indices de homicidio y sacamos lor promedios de todos los años
#de los que hay datos
crimes = crimes[crimes["Series"] == "Intentional homicide rates per 100,000"].groupby("Región").mean()
#%%
#En esta celda obtenemos los 3 paises con mayor indice de homicidios promedio
max_crime = pd.DataFrame()
max_crime["Value"] = crimes["Value"].nlargest(3)
max_crime["Región"] = crimes["Value"].nlargest(3).index
max_crime.to_csv("./Datos_filtrados/Los 3 países con mayor indice promedio de criminalidad.csv")
name_crime_max = max_crime["Región"]
#%%
#En esta celda obtenemos los 3 paises con menor indice de homicidios promedio
min_crime = pd.DataFrame()
min_crime["Value"] = crimes["Value"].nsmallest(3)
min_crime["Región"] = crimes["Value"].nsmallest(3).index
min_crime.to_csv("./Datos_filtrados/Los 3 países con menor indice promedio de criminalidad.csv")
name_crime_min = min_crime["Región"]
#%%
#En esta celda se grafica los datos optenidos 
fig, axes = plt.subplots(1,2,figsize=(15,6))
axes[0].bar(name_crime_max,max_crime["Value"])
axes[0].set_title("Países con mayor índice de criminalidad")
axes[0].set_xlabel("País")
axes[0].set_ylabel("Índice de criminalidad")
axes[1].bar(name_crime_min,min_crime["Value"])
axes[1].set_title("Países con menor índice de criminalidad")
axes[1].set_xlabel("País")
axes[1].set_ylabel("Índice de criminalidad")
fig.savefig("./Gráficas/países_mayor_menor_indice_crimenes.pdf")
#%%
#En esta celda leemos los datos de los dos archivos restantes a analizar
#el primero es el GNI per capita y el segundo el ratio de inscripción a escuelas secundarios 
GNI_per_capita = pd.read_csv("./Datos/GNI_per_capita.csv")
Gross_enrolment_ratio_Secondary_education = pd.read_csv("./Datos/Gross_enrolment_ratio_Secondary_education.csv")
#%%
#En esta celda se extraen los datos de los paises obtenidos en la segunda y tercera celda de la tabla GNI per capita 
GNI_crime_max = GNI_per_capita[(GNI_per_capita["Country or Area"] == name_crime_max[0]) | (GNI_per_capita["Country or Area"] == name_crime_max[1]) | (GNI_per_capita["Country or Area"] == name_crime_max[2])]
GNI_crime_min = GNI_per_capita[(GNI_per_capita["Country or Area"] == name_crime_min[0]) | (GNI_per_capita["Country or Area"] == name_crime_min[1]) | (GNI_per_capita["Country or Area"] == name_crime_min[2])]
GNI_crime_max.to_csv("./Datos_filtrados/GNI per capita de los 3 países con mas crimen.csv")
GNI_crime_min.to_csv("./Datos_filtrados/GNI per capita de los 3 países con menos crimen.csv")
#%%
#En esta celda se extraen los datos de los paises obtenidos en la segunda y tercera celda de la tabla Gross enrolment ratio secondary education
Secondary_crime_max = Gross_enrolment_ratio_Secondary_education[(Gross_enrolment_ratio_Secondary_education["Sex"] == "All genders") & ((Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime_max[0]) | (Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime_max[1]) | (Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime_max[2]))]
Secondary_crime_min = Gross_enrolment_ratio_Secondary_education[(Gross_enrolment_ratio_Secondary_education["Sex"] == "All genders") & ((Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime_min[0]) | (Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime_min[1]) | (Gross_enrolment_ratio_Secondary_education["Reference Area"] == name_crime_min[2]))]
Secondary_crime_max.to_csv("./Datos_filtrados/Ratio de inscripción a secundaria de los 3 países con mayor criminalidad.csv")
Secondary_crime_min.to_csv("./Datos_filtrados/Ratio de inscripción a secundaria de los 3 países con menor criminalidad.csv")
#%%
#En esta celda se grafica la variación del GNI per capita de los tres países con mayor y menor indice de criminalidad 
fig, axes = plt.subplots(figsize=(30,6))
GNI_crime_0 = GNI_crime_max[GNI_crime_max["Country or Area"] == name_crime_max[0]].sort_values(by='Year', ascending=True)
GNI_crime_1 = GNI_crime_max[GNI_crime_max["Country or Area"] == name_crime_max[1]].sort_values(by='Year', ascending=True)
GNI_crime_2 = GNI_crime_max[GNI_crime_max["Country or Area"] == name_crime_max[2]].sort_values(by='Year', ascending=True)
GNI_crime_3 = GNI_crime_min[GNI_crime_min["Country or Area"] == name_crime_min[0]].sort_values(by='Year', ascending=True)
GNI_crime_4 = GNI_crime_min[GNI_crime_min["Country or Area"] == name_crime_min[1]].sort_values(by='Year', ascending=True)
GNI_crime_5 = GNI_crime_min[GNI_crime_min["Country or Area"] == name_crime_min[2]].sort_values(by='Year', ascending=True)
axes.plot(GNI_crime_0["Year"], GNI_crime_0["Value"],"bo-",label=name_crime_max[0])
axes.plot(GNI_crime_1["Year"], GNI_crime_1["Value"],"ro-",label=name_crime_max[1])
axes.plot(GNI_crime_2["Year"], GNI_crime_2["Value"],"go-",label=name_crime_max[2])
axes.plot(GNI_crime_3["Year"], GNI_crime_3["Value"],"ko-",label=name_crime_min[0])
axes.plot(GNI_crime_4["Year"], GNI_crime_4["Value"],"mo-",label=name_crime_min[1])
axes.plot(GNI_crime_5["Year"], GNI_crime_5["Value"],"yo-",label=name_crime_min[2])
axes.set_title("Variación del GNI per capita de los 3 países con mayor y menor índice de criminalidad")
axes.set_xlabel("Año")
axes.set_ylabel("GNI per capita")
axes.legend(loc="upper left")
fig.savefig("./Gráficas/Variación del GNI per capita de los 3 países con mayor y menor índice de criminalidad.pdf")
#%%
#En esta celda se grafica la variación del porcentaje de inscripción a educación secundaria
#de los tres países con mayor y menor indice de criminalidad 
fig, axes = plt.subplots(figsize=(30,6))
Seconda_crime_0 = Secondary_crime_max[Secondary_crime_max["Reference Area"] == name_crime_max[0]].sort_values(by='Time Period', ascending=True)
Seconda_crime_1 = Secondary_crime_max[Secondary_crime_max["Reference Area"] == name_crime_max[1]].sort_values(by='Time Period', ascending=True)
Seconda_crime_2 = Secondary_crime_max[Secondary_crime_max["Reference Area"] == name_crime_max[2]].sort_values(by='Time Period', ascending=True)
Seconda_crime_3 = Secondary_crime_min[Secondary_crime_min["Reference Area"] == name_crime_min[0]].sort_values(by='Time Period', ascending=True)
Seconda_crime_4 = Secondary_crime_min[Secondary_crime_min["Reference Area"] == name_crime_min[1]].sort_values(by='Time Period', ascending=True)
Seconda_crime_5 = Secondary_crime_min[Secondary_crime_min["Reference Area"] == name_crime_min[2]].sort_values(by='Time Period', ascending=True)
axes.plot(Seconda_crime_0["Time Period"], Seconda_crime_0["Observation Value"],"bo-",label=name_crime_max[0])
axes.plot(Seconda_crime_1["Time Period"], Seconda_crime_1["Observation Value"],"ro-",label=name_crime_max[1])
axes.plot(Seconda_crime_2["Time Period"], Seconda_crime_2["Observation Value"],"go-",label=name_crime_max[2])
axes.plot(Seconda_crime_3["Time Period"], Seconda_crime_3["Observation Value"],"ko-",label=name_crime_min[0])
axes.plot(Seconda_crime_4["Time Period"], Seconda_crime_4["Observation Value"],"mo-",label=name_crime_min[1])
axes.plot(Seconda_crime_5["Time Period"], Seconda_crime_5["Observation Value"],"yo-",label=name_crime_min[2])
axes.set_title("Variación del número de ingresos a educación secundaria de los 3 países con mayor y menor índice de criminalidad")
axes.set_xlabel("Año")
axes.set_ylabel("Iscripciones a educación secundaria")
axes.legend(loc="upper left")
fig.savefig("./Gráficas/Variación de ingresos a educación secundaria de los 3 países con mayor y menor índice de criminalidad.pdf")