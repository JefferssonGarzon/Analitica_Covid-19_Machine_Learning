import numpy as np

data_pt2 = np.loadtxt("DataS.txt")
print(data_pt2, "\n")



x = data_pt2[0]
y = data_pt2[1]

"""

# El promedio ponderado por volumen (VWAP)

print(x)
print(y)

vwap =  np.average(x, weights=y)
print("VWAP =", vwap)

# TWAP otra medida


"""
# calculo de los valores maximo y minimo

print("Maximos casos por día: ", np.max(y))
print("Minimos casos por día: ", np.min(y))

# calcular la extensión de una matriz ptp

print("Extension de numeros de casos", np.ptp(y))


