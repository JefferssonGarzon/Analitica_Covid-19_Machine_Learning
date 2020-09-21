import numpy as np 
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt


#data = np.genfromtxt("covid.tsv", delimiter= "\t")
# sacamos el dataset con pandas
df = pd.read_csv("C:/Users/Jefferson/Desktop/Computacion_Blanda/DATOS/covid.tsv", sep="\t") 
print(df[:2], "\n")

# ordenamos la columna de Fechas
orden = df.sort_values("Fecha de notificación")
data_F = orden["Fecha de notificación"]

print("Fecha de notificacion: \n", data_F)

F_init = data_F[0] # punto de partida
print(F_init)

n = 0
dates = []
num = []


# conteo de numeros de casos en un cierto dia
datos = [dates, num]
for fechas in data_F:
    if fechas == F_init:
        n+=1
       
    else:
        datos[0].append(F_init)
        datos[1].append(n)
        F_init = fechas
        n = 1
        #print("nuevo indicador: ", F_init)
    


 
#limpiar una columna (Fechas)

datos[0].clear()
b = 1
tamaño = len(datos[1])
print(tamaño)

# ingresamos de forma ascendente los dias
while (b-1) < tamaño:
    datos[0].append(b)
    b += 1

x = np.array(datos[0]) # tipo int COLUMNA DIAS
y = np.array(datos[1]) # tipo int COLUMNAS NUMERO DE INFECTADOS


print(x, "\n") #numero de dias
#print("dimension: \n", x.ndim)

print("tipo de dato X: ", type(x[0]))
print("tipo de dato X: ", x.shape)
print("tipo de dato Y: ", type(y[0]))
print("tipo de dato Y: ", y.shape)
print(x, "\n")
print(y, "\n")

# Investigamos el número de valores nan que contiene el vect x

print("Valores nan en X: ",np.sum(np.isnan(x)))
print("valores nan en Y: ",np.sum(np.isnan(y)))

# SE COMIENZA A GRAFICAR -------------

# Dibuja los puntos (x,y) con círculos de tamaño 10
plt.scatter(x, y, s=10)

# titulos de la grafica
plt.title("Numero de casos por día")
plt.xlabel("Semana")
plt.ylabel("# de casos")

plt.xticks([w*24 for w in range(10)],['S %i' % w for w in range(10)])
plt.autoscale(tight = False)

# dibuja una cuadrícula punteada ligeramente opaca
plt.grid(True, linestyle='-', color='0.75')

# Muestra el gráfico
plt.show()


z = [x,y]
print(type(z))



# convierto a tipo numpy array 
w = np.array(z)
print(type(w))

np.savetxt("DataS.txt", w)


        