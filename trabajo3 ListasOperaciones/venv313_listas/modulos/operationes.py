#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 09/06/2024                     #
#***************************************#

#Este programa nos muestra la funcionalidad de las listas en python, mediante un 
# numero aleatorio generado por randint, el programa genera un lista de numeros 
# con los cuales hace diferentes operaciones, ademas de mostrarnos la longitud de
#la lista, los numeros pares e impares.

import random

def operator(): # La funcion de operator encaragada de toda la parte pricipal del programa 
    randomList = [] # Lista vacia para generar numeros aleatorios
    lista_pares = [] # Lista vacia para numeros pares
    lista_impares = [] # Lista vacia para numeros impares 
    suma = 0 # Inicializo variable suma 

    while True:
        n = random.randint(0,20) # Funcion generador de listas de numeros aleatorios de 0 a 20
        if n == 0 :       # Si el numero generado aleatoriamente es cero el programa se cierra
            break
        randomList.append(n)# De acuerdo al numero generado se crae la lista de numeros aletorios
                          
    for n in randomList: # Funcion para generar listas de numeros pares e impares
        if n%2 == 0 :
         lista_pares.append(n)#  Con el if se logra  generar listas de numeros pares 
        else: 
            lista_impares.append(n)   #Con el else se logra  generar listas de numeros pares 

    for n in range(0, len(randomList)): # De acuerdo a longitud y los numeros se pueden realizar las operaciones 
        suma = suma + randomList[n] # Funcion suma y promedio 
        promedio = suma / len(randomList)

    print(randomList)
    print(f"la lista tiene {len(randomList)} elementos ") # Print que muestra la longitud de la lista 
    print(f"La suma de todos los numeros es: {suma}")   # Print que muestra la suma de los elementos 
    print(f"El promedio de la lista es: {int(promedio)}") # Print que muestra el promedio de la lista de numeros 
    print(f"los numeros pares son: {lista_pares}") # Print que muestra la lista de numeros pares 
    print(f"los numeros impares son : {lista_impares}")# Print que muestra la lista de numeros impares 


        