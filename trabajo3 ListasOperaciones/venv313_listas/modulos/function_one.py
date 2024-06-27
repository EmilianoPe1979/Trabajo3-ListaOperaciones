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
from modulos import operationes as oper  # Importo la funcion operaciones

def respuesta(): # Defino la funcion respuesta 
    
    while True: # Bucle para repetir la operacion de LISTAS
       
        respuesta = input ("Desea continuar con las tablas si/no:  ")
        # Pregunta si deseo o no continuar con la operacion de listas 

        while respuesta not in ["si", "no"]:
            print("Ingrese SI o NO")
            respuesta = control_letras("Desea continuar generando listas si/no: ")
        # Se define la respuesta SI/NO 

        if respuesta == "si": # Respuesta SI llame operator listas 
            oper.operator()
            
        elif respuesta == "no": # Respuesta NO fin del programa 
            print("FIN DEL PROGRAMA")
            break   # Si respuesta es no se rompe el ciclo del bucle y se sale del programa         
        else:
            continue # Si no entonces vuelva la programa y realice el ciclo nuevamente 
            break

def control_letras(prompt): # Funcion de control de entrada 
    while True: # Declaracion de while con la condicion de entrada 
      entrada = input(prompt)
      if (entrada.replace("","").isalpha()): #La entrada solo acepra caracteres alafabeticos 
        break # Declaracion para detener el ciclo while 
      else:
        print("Solo digite caracteres alfabeticos")# mensaje en caso de que la entrada sea diferente a cacateres alfabeticos 
    return entrada # Retorna a la entrda del ciclo 

  