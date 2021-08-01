# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:24:05 2021

@author: Wilson Quito
"""

lista=["R1","R2","R3","R4","S1","S2" ]
lista_s=[]
lista_r=[]
for i in lista:
    if "S" in i:
        lista_s.append(i)
print("Lista con datos de S")        
print(lista_s)
for i in lista:
    if "R" in i:
        lista_r.append(i)
print(" ")
print("Lista con datos de R")
print(lista_r)


lista=["R1","R2","R3","R4","S1","S2" ]
lista_s=[]
lista_r=[]
for i in lista:
    if "S" in i:
        lista_s.append(i)
    if "R" in i:
        lista_r.append(i)
print("Lista con datos de S")        
print(lista_s)
print(" ")
print("Lista con datos de R")
print(lista_r)


lista=["R1","R2","R3","R4","S1","S2" ]
lista_s=[]
lista_r=[]
for i in lista:
    if "S" in i:
        lista_s.append(i)
    else:
        lista_r.append(i)
print("Lista con datos de S")        
print(lista_s)
print(" ")
print("Lista con datos de R")
print(lista_r)