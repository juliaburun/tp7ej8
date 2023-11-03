#﻿Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa.
#Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las
#que se encuentre. La carga de datos termina cuando se obtenga un 0 como número al azar,el que no deberá cargarse en la lista.

import random



def cargar_lista():
    
    lista = []
    n = random.randint(0, 100)
    
    while n != 0:
        lista.append(n)
        n = random.randint(0, 100)
        
    return lista

def encontrar_menor(lista):
    largo = len(lista)
    menor = lista[0]
    posiciones = []
        
    for i in range(largo):
        if lista[i] < menor:
            menor = lista[i]            
    
    for i in range(largo):
        if menor == lista[i]:
            posiciones.append(i)
    
    return menor, posiciones

def imprimir(menor, posiciones):

    print("El menor es:", menor, "y su/s posicion/es es/son: ", posiciones)
    
        
#Programa principal
c = cargar_lista()
a, b = encontrar_menor(c)
imprimir(a, b)
        
            

