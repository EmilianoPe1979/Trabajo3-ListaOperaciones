
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
from colorama import Fore,Back # Importo colorama para color fondo y fuente
from modulos import operationes as oper  # importo modulo operaciones 
from modulos import function_one as fun # importo modulo respuesta 

def main():
  
  print(Fore.BLACK + Back.BLUE)
  oper.operator() # llamo generador me entrega lista de numeros aleatorio 
  fun.respuesta() # llamo generador respuestas
  
  
if __name__ == "__main__": # Indica que app es el programa principal 
  main()

 


    