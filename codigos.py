#Importamos las librerias en general para todos los códigos
import numpy as np
import sympy as sym #Para crear la expresion 
import matplotlib.pyplot as plt

# Ingreso de datos, pero acá están presentados como listas
datos = np.loadtxt(r'C:\Users\Susana Rodriguez\Documents\Universidad-IUE\Septimo Semestre-Ingeniería Informática\Métodos Numéricos\Tarea\Tarea 2\datos.txt')
xid = datos[:,0] 
fid = datos[:,1] 

def polinomica(x,y):
    
    # Procedimiento, pasamos a convertirlos en arreglos
    xi = np.array(xid)
    fi = np.array(fid)
    B = np.copy (fi)

    #Matriz
    n = len(xi) #Tamaño de la matriz
    D = np.zeros((n,n),dtype=float) #Matriz, llena de ceros
    ultima = n-1

    #Para llenar las casillas
    i = 0 #Fila cero
    for i in range(0,n,1): #mover el valor de i, en el rango desde la primera hasta la ultima
        for j in range(0,n,1): #mover el valor de j, en el rango desde la primera hasta la ultima
            potencia = ultima -j #Se calcula el valor de la exponente,ultima columna menos la posicion de la columna en la que voy avanzando
            D[i,j] = xi[i] **potencia #Posicion en la matriz

    # Calculo de coeficientes del polinomio,mediante algebra lineal
    coeficientes = np.linalg.solve(D,B)#Matriz y vector

    #Polinomio de Interpolación
    x = sym.Symbol('x') # X va a ser tomada como un simbolo
    polinomio = 0 #Comenzamos con polinomio vacío
    for i in range(0,n,1): #Se mueve desde la primera hasta la ultima en pasos de uno
        potencia = (n-1)-i #Es relativo al valor de la ultima posición
        termino = coeficientes[i]*(x**potencia)
        polinomio = polinomio + termino

    #Para facilitar la evaluación del polinomio
    px = sym.lambdify(x,polinomio)
    #Evaluar polinomio
    muestras = 51 #muestras suficientes para que la linea no tenga distorcion en la grafica
    a = np.min(xi) #Minimo
    b= np.max(xi) #Máximo
    pxi = np.linspace(a,b,muestras) #Serie de puntos muestreados
    pfi = px(pxi) #puntos de la función,usando la forma numerica del polinomio

    #Evaluamos en 2.5 para ver la dosificación
    print('Resultado de la dosificación en 2.5: ', px(2.5))
    #Salida
    print ('Matriz')
    print ('D')
    print ('Coeficientes:')
    print (coeficientes)
    print ('polinomio: ')
    print (polinomio)
    #crearemos una grafica
    plt.plot(2.5,px(2.5),'o', label='2.5')
    plt.plot(xi,fi,'o', label='puntos')
    plt.grid()
    plt.plot(pxi,pfi, label='polinomio') #Trazamos la linea de los puntos
    plt.legend() #Mostrar todas las etiquetas
    plt.title('Polinomio de Interpolación')#Añadimos un titulo
    plt.show() #Para ver la gráfica

  

#-----------------------------------------------------------------------------