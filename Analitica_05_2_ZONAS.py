import numpy as np
import matplotlib.pyplot as plt
import sys

data = np.loadtxt("DataS.txt")
print(data)

x = data[0]
print("x: ",x)
y = data[1]

print("tipo: ", type(data[0]))
# AJUSTE UTILIZANDO DOS ZONAS - Grado 1 

plt.scatter(x, y, s=10)

plt.title("Numero de casos Covid-19")
plt.xlabel("Semanas")
plt.ylabel("# de casos")

plt.xticks([w*23.85 for w in range(10)],['S %i' % w for w in range(10)])
plt.autoscale(tight = False)

plt.grid(True, linestyle='-', color='0.75')

def error(f, x, y):
    return np.sum((f(x)-y)**2)

# calcular el punto de inflexion 
inflexion = 90

xa = x[:int(inflexion)] # Datos antes del punto de inflexión
ya = y[:int(inflexion)]

xb = x[int(inflexion):] # Datos después del punto de inflexión
yb = y[int(inflexion):]


print("xa: ", xa)
print("ya: ", ya)

print("xb: ", xb)
print("yb: ", yb)



fa = np.poly1d(np.polyfit(xa, ya, 1))
fb = np.poly1d(np.polyfit(xb, yb, 1))

fx = np.linspace(0,x[-1])
plt.plot(fx, fa(fx), linewidth=4, color="red")
plt.plot(fx, fb(fx), linewidth=4, color="yellow")
fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print("Error de inflexión = %f" % (fa_error + fb_error))

plt.show()