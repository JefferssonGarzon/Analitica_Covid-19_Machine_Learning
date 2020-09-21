# AJUSTES POLINOMIALES
# -----------------------------------------------------------------
# Lección 06
#
# ** Se importan los archivos de trabajo
# ** Se crean las variables
# ** Se generan los modelos
# ** Se grafican las funciones

# Se importa la librería del Sistema Operativo
# Igualmente, la librería utils y numpy
# -----------------------------------------------------------------
import os

# Directorios: chart y data en el directorio de trabajo
# -----------------------------------------------------------------
from utils import DATA_DIR, CHART_DIR
import numpy as np

# Se eliminan las advertencias por el uso de funciones que
# en el futuro cambiarán
# -----------------------------------------------------------------
np.seterr(all='ignore')

# Se importa la librería scipy y matplotlib
# -----------------------------------------------------------------
import scipy as sp
import matplotlib.pyplot as plt

data = np.loadtxt(os.path.join(DATA_DIR, "C:/Users/Jefferson/Desktop/Computacion_Blanda/DataS.txt"))
#data = np.genfromtxt(os.path.join(DATA_DIR, "C:/Users/Jefferson/Desktop/Computacion_Blanda/DataS.txt"), delimiter="\n")

#se establece el tipo de dato
data = np.array(data, dtype= np.float64)
print("Datos: ",data[:10])
print("Tipo: ",type(data))

