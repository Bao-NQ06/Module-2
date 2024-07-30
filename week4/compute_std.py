import numpy as np

def compute_std ( X ) :
    variance = np.var(X)
    return np . sqrt ( variance )

X = [ 171 , 176 , 155 , 167 , 169 , 182]
print ( compute_std ( X ) )