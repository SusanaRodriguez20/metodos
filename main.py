#Importamos las librerias en general para todos los códigos
import numpy as np
import sympy as sym #Para crear la expresion 
import matplotlib.pyplot as plt
import codigos as cod

#Polinomial
datos = np.loadtxt(r'C:\Users\Susana Rodriguez\Documents\Universidad-IUE\Septimo Semestre-Ingeniería Informática\Métodos Numéricos\Tarea\Tarea 2\datos.txt')
xid = datos[:,0] 
fid = datos[:,1] 
terminar = 0
cod.polinomica(xid,fid)


while(terminar == 0):
    hacer = int(input("Que quieres hacer? \n 1: Método Polinomial \n 2: Método de Lagrange \n 3: Método de Newton \n 4: Método de Trazadores Cuádraticos \n 5: Funciones de Base Radial \n 6: Salir \n Ingrese el numero: "))

    if(hacer == 1):
        cod.codigos(xid,fid)

