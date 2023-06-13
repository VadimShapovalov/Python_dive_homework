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


