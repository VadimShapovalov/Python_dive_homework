# Напишите функцию для транспонирования матрицы


def matrix_transposition(matrix: list):
    """ function to transpose a matrix. """
    trans_matrix = []
    for i in range(len(matrix)):
        trans_matrix.append([matrix[j][i] for j in range(len(matrix[i]))])
    return trans_matrix


original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Оригинальная матрица:")
print(*original_matrix, sep='\n', end='\n\n')
print(f"Транспонированная матрица:")
print(*matrix_transposition(original_matrix), sep='\n')

# trans_matrix2 = []
# for i in range(len(original_matrix)):
#     for j in range(len(original_matrix)):
#         trans_matrix2[i][j] = original_matrix[i][j]
#
# print(*matrix_transposition(original_matrix), sep='\n')

# trans_matrix = []
# for i in range(len(original_matrix)):
#     trans_matrix.append([original_matrix[2-j][i] for j in range(len(original_matrix[i]))])
# print(*trans_matrix, sep='\n')