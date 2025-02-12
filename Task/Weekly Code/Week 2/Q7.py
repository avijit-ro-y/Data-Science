import numpy as np
def mat(matr):
    matrix1 =np.array(matr)
    reverse=matrix1[::-1]
    transpose=reverse.T
    return transpose

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(mat(matrix))
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(mat(matrix))
