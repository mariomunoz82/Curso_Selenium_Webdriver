# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:44:48 2023

@author: MARIO
"""

#Introduccion a las variables

a=10
b=20

suma=a+b
print("La suma es: ",suma)

nombre1="Mario"
Nombre2="Alexis"
Apellido1="Muñoz"

print("Tu nombre {}, tu segundo nombre {} tu primer apellido {} ".format(nombre1,Nombre2,Apellido1))


a=int(input("Numero1: "))
b=int(input("Numero2: "))

suma=a+b
print(suma)

lista1=[]
lista2=[]
lista3=[]

def ingresovariables(num1,num2):
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b "))
    if a>b:
        try:
            divisor=a/b
            lista1.append(divisor)
        except ZeroDivisionError:
            print("No puedes dividir entre 0")
    elif a<b:
         producto=a*b
         lista2.append(producto)
    else:
        potencia=a**b
        lista3.append(potencia)
    print("fin del proceso")
        
ingresovariables(a,b)

print(lista1)
print(lista2)
print(lista3)    


            
    