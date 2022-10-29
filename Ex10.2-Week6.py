# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:02:47 2019

@author: USUARIO
"""

filename = input("Enter file name: ")
filehandle = open(filename)
dictio = dict()

#Ciclo para encontrar hora de mayor frecuencia, 
# de envío de correos despúes de la palabra From
#usando la funcion diccionario

for X in filehandle:
    if "From" in X:
        especificword = X.split()
        if especificword[0] == "From":
            hora = especificword[5]
            marca1 = hora.find(":")
            marca2 = hora[0:marca1]
            dictio[marca2] = dictio.get(marca2,0)+1
                  
t = sorted(dictio.items())
for key,value in t:
    print(key, value)
                