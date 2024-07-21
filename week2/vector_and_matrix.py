import numpy as np
def compute_vector_length ( vector ) :
    
    len_of_vector= np.linalg.norm(vector)

    return len_of_vector


def compute_dot_product ( vector1 , vector2 ) :
    result = sum(x*y for x,y in zip(vector1,vector2))
    return result

vector1 = np.array([3,4])
vector2 = np.array([4,5,6,7])




print(compute_vector_length(vector1))
print(compute_dot_product(vector1=vector1, vector2=vector2))


def matrix_multi_vector ( matrix , vector ) :
    matrix = np.array(matrix)
    vector = np.array(vector)

    result = matrix @ vector
    return result


m = np. array ([[ -1 , 1 , 1] , [0 , -4 , 9]])
v = np. array ([0 , 2 , 1])
result = matrix_multi_vector (m, v)
print ( result )




def matrix_multi_matrix ( matrix1 , matrix2 ) :
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    result = matrix1 @ matrix2
    return result


m1 = np. array ([[0 , 1 , 2] , [2 , -3 , 1]])
m2 = np. array ([[1 , -3] ,[6 , 1] , [0 , -1]])
result = matrix_multi_matrix (m1 , m2)
print ( result )



def inverse_matrix(matrix):
    matrix = np.array(matrix)
    determinant = np.linalg.det(matrix)
    if determinant == 0:
        return 'This matrix is not invertible'
    else:
        return np.linalg.inv(matrix)
    
m1 = np. array ([[ -2 , 6] , [8 , -4]])
result = inverse_matrix(m1)
print ( result )