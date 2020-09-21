import numpy as np
import matplotlib.pyplot as plt

# Lección 05
#
# Proyecto básico de machine learning
# Manejo de datos
# Graficación de datos

data = np.loadtxt("DataS.txt")
print("primeros 10 datos: ", data[:10], "\n")

# Numero de datos
print("Numero de datos: ",data.shape)

x = data[0]
y = data[1]

print("x: ", x)
print("y: ", y)

# Verificación de los datos generados
# Dimensión de los vectores x, y
# --------------------------------------------------------------
print("dimension de x: ",x.ndim)
print("dimension de y: ",y.ndim)

# Investigamos el número de valores, tipo nan, que contiene el vector
# --------------------------------------------------------------
print(np.sum(np.isnan(y)))

#BÚSQUEDA PREDICTIVA EN EL ENTORNO numpy DE python

# DESDE AQUI SE COMIENZA A GRAFICAR
# EL CÓDIGO, A PARTIR DE ESTE PUNTO, ES EL QUE SE ESTUDIO PREVIAMENTE

# Se dibuja, de manera abstracta, el punto (x,y)
# con círculos de tamaño 10
# --------------------------------------------------------------
plt.scatter(x, y, s=10)

# Títulos del gráfico
# --------------------------------------------------------------
plt.title("Numero de casos Covid-19")
plt.xlabel("Semanas")
plt.ylabel("# de casos")

# Se dibujan las marcas del gráfico
# --------------------------------------------------------------
plt.xticks([w*23.85 for w in range(10)],['S %i' % w for w in range(10)])
plt.autoscale(tight = False)

# dibuja una cuadrícula punteada ligeramente opaca
# --------------------------------------------------------------
plt.grid(True, linestyle='-', color='0.75')

# EL CÓDIGO REUTILIZADO TERMINA AQUÍ. A PARTIR DE ESTE PUNTO SE GENERAN
# NUEVAS INSTRUCCIONES PARA EL AJUSTE DE LA CURVA

# Función que calcula el error (vector)
def error(f , x, y):
    return np.sum((f(x)-y)**2)


# A CONTINUACIÓN SE UTILIZA LA FUNCIÓN DE AJUSTE POLINOMIAL

# fp1 (parámetros de la función respuesta)
# residuals, que es el error del ajuste realizado
# Ambos valores serán estudiados más abajo en el documento
# --------------------------------------------------------------
fp1, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)

print("Parámetros del modelo: %s" % fp1, '\n')

print("Error devuelto por el ajuste:", residuals, '\n')

# Mediante la función poly1d, se crea la recta a partir de
# los parámetros generados por el ajuste (disponibles en fp1)
# --------------------------------------------------------------
f1 = np.poly1d(fp1)

# Error después de generar la recta (igual al recibido)
# --------------------------------------------------------------
print("Error después de generar la recta:", error(f1, x, y), '\n')

# Se dibuja la recta que se ajusta a los puntos
# --------------------------------------------------------------
# linespace
# --------------------------------------------------------------
# Se utiliza la función: linspace.
# El primer parámetro es el primer valor a utilizar en x,
# que para nuestro caso es el valor cero.

# El siguiente parámetro es es el último valor en x, que para nuestro
# caso se encuentra en la posición final de x.
# Puesto que se x inicia en la posición 0, el último valor se obtiene
# en la posición (x - 1), lo cual explica la instrucción x[-1]
# El tercer parámetro, 1000, indica el número de divisiones a
# realizar en cuanto a los puntos tomados. Para nuestro ejemplo,
# basta con que dicho valor no sea negativo. Otros valores diferentes a 1000
# funcionan igualmente bien.
# --------------------------------------------------------------
fx = np.linspace(0,x[-1], 1000)

# Se generan los puntos verticales. A partir de fx, se calculan
# los valores en y: f1(fx). Los otros parámetros se autoexplican
# --------------------------------------------------------------
plt.plot(fx, f1(fx), linewidth=4, color="red")
# Se muestra en la esquina superior izquierda (upper left)
# el grado del polinomio del ajuste (1 = línea recta)
# --------------------------------------------------------------
"""plt.legend(["Grado d=%i" % f1.order], loc="upper left")"""


# POLINOMIO DE GRADO 2

# NOTA: En la función polyfit, el valor 2, como parámetro,
# hace referencia a un polinomio de segundo grado
# ----------------------------------------------------------------
f2p = np.polyfit(x, y, 2)
print("Parámetros del modelo: %s" % f2p)
print("Ecuación: f(x) = 0.0105322215 * x**2 - 5.26545650 * x + 1974.76082\n")
# Se genera la gráfica
# ----------------------------------------------------------------
f2 = np.poly1d(f2p)
# Error después de generar la gráfica
# ----------------------------------------------------------------
print("Error después de generar la curva:",error(f2, x, y))
# Se realiza la gráfica de salida (sobre las anteriores)
# ----------------------------------------------------------------

#plt.plot(fx, f2(fx), linewidth=4, color="yellow")

# Se agrega un texto explicativo sobre el grado utilizado
# Se escriben ambos valores para grado 1 y grado 2 en la
# misma instrucción
# ----------------------------------------------------------------
"""plt.legend(["Grado d=%i\n" % f1.order, "Grado d=%i" % f2.order],
loc="upper left")"""

# ESPACIO PARA MOSTRAR (insert plt.show())

# GRADO 3 Y 10

f3p = np.polyfit(x, y, 3)
f3 = np.poly1d(f3p)
#plt.plot(fx, f3(fx), linewidth=4, color="green")

f10p = np.polyfit(x, y, 10)
f10 = np.poly1d(f10p)
#plt.plot(fx, f10(fx), linewidth=2, color="black")

"""plt.legend(["Grado d=%i" % f1.order, "Grado d=%i" % f2.order,
"Grado d=%i" % f3.order, "Grado d=%i" % f10.order],
loc="upper left")"""

# GRADO 1 Y 53

f53p = np.polyfit(x, y, 53)
f53 = np.poly1d(f53p)
plt.plot(fx, f53(fx), linewidth=4, color="#ffff00")

plt.legend(["Grado d=%i" % f1.order, "Grado d=%i" % f53.order],
loc="upper left")




plt.show()
