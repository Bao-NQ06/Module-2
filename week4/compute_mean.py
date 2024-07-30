import numpy as np

def compute_mean ( X ) :
    mean_x = np.mean(np.array(X))
    return mean_x

X = [2 , 0 , 2 , 2 , 7, 4 , -2 , 5 , -1 , -1]

print (" Mean : ", compute_mean ( X ) )