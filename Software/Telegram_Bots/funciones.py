import pandas as pd
import numpy as np

def funcion_externa():
    DataFrame = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['Col a', 'Col b', 'Col c'])
    
    return str(DataFrame)