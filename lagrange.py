import matplotlib.pyplot as plt
import numpy as np

# Carga de datos
datos = np.loadtxt(r'C:\Users\Susana Rodriguez\Documents\Universidad-IUE\Septimo Semestre-Ingeniería Informática\Métodos Numéricos\Tarea\Tarea 2\datos.txt')
xdat = datos[:,0]
ydat = datos[:,1]
xy = []

for i in range(0,len(datos)):
    xdat = datos[i,0]
    ydat = datos[i,1]
    xy.append((xdat,ydat)) 

# Cálculo de los coeficientes de Lagrange
def lagrange_coefficients(xy):
    
    n = len(xy)
    coefficients = []
    for i in range(n):
        xi, yi = xy[i]
        Ai = yi
        for j in range(n):
         if i != j:  # Excluye el punto actual
          xj, _ = xy[j]
        try:
            Ai /= (xi - xj)
        except ZeroDivisionError:
            Ai = 0
        coefficients.append(Ai)
    return coefficients

# Cálculo del polinomio interpolante
def lagrange_polynomial(x, xy, coefficients):
    n = len(xy)
    y = 0
    for i in range(n):
        xi, _ = xy[i]
        Ai = coefficients[i]
        term = Ai
        for j in range(n):
            if i != j:
                xj, _ = xy[j]
                term *= (x - xj)
        y += term
    return y


# Graficación
plt.figure()
coefficients = lagrange_coefficients(xy)
# Lagrange
x_values = np.arange(0, 4.05, 0.05)
y_values = [lagrange_polynomial(x, xy, coefficients) for x in x_values]
plt.plot(x_values, y_values, color='black',label="Polinomio de Lagrange")
plt.scatter(*zip(*xy), color='green', label="Puntos dados")


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Interpolación con funciones de base radial')

plt.show()
