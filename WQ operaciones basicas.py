# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Wilson Quito
"""
def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def mult(x, y):
    return x * y
def div(x, y):
    return x / y
print("Operaciónes")
print("1 Suma")
print("2 Resta")
print("3 Multiplicar")
print("4 Dividir")
signo = input("Seleccione la operación ( 1 | 2 | 3 | 4 ): ")
if signo=="1" or signo=="2" or signo=="3" or signo=="4":
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    TR=("El resulado de:")
    print("\n")
    if signo == "1":
        print(TR,n1,"+",n2,"es", suma(n1,n2))
    elif signo == "2":
        print(TR,n1,"-",n2,"es", resta(n1,n2))
    elif signo == "3":
        print(TR,n1,"*",n2,"es", mult(n1,n2))
    elif signo == "4":
        print(TR,n1,"/",n2,"es", div(n1,n2))
else:
    print("Operación no disponible")

