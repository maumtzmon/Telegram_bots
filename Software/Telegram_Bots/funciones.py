########################################################################
#
# Plantilla de funciones basicas adicionales del bot de Telegram
# Ing. Mauricio Martinez Montero
# LabDet, Criogenia. Instituto de Ciencias Nucleares, UNAM.
#
# Pequeña plantilla que contiene funciones de analisis y procesos
# en ella podemos programar lo que sea y devolver el resultado en 
# formato string para desplegarla como un mensaje en la interfaz de 
# Telegram
#
#
########################################################################


import pandas as pd
import numpy as np

def funcion_externa():
    DataFrame = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['Col a', 'Col b', 'Col c'])
    
    return str(DataFrame)

def AlertTest():
    DataFrame = pd.DataFrame(np.array([[0, 0, 'X'], [0, 'X', 0], ['X', 0, 0]]),columns=['Col a', 'Col b', 'Col c'])
    return str(DataFrame)