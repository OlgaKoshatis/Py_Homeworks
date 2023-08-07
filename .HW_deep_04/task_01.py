#Напишите функцию для транспонирования матрицы

import numpy as np

def matrix_transpose(n, m):
    matrix_orig = np.random.randint(1, 10, size=(n, m))
    print('Исходная матрица:\n', matrix_orig)
    matrix_trans = np.zeros((m, n), int)
    for i in range(len(matrix_orig)):
        for j in range(len(matrix_orig[i])):
            matrix_trans[j][i] = matrix_orig[i][j]
    
    return matrix_trans
    
print('Транспонированная матрица:\n', matrix_transpose(int(input('rows:\t')), int(input('cols:\t'))))

