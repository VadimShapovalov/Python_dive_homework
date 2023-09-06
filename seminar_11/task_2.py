# Создайте класс Матрица. Добавьте методы для вывода на печать:
# - вывода на печать, - сравнения, - сложения, - *умножения матриц

class EquilateralMatrix:
    """the class of equilateral matrices"""

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def __str__(self):
        return '\n'.join(['  '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError('Матрицы должны быть одинакового размера.')
        new_matr = EquilateralMatrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                new_matr.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return new_matr

    def __sub__(self, other):
        if self.size != other.size:
            raise ValueError('Матрицы должны быть одинакового размера.')
        new_matr = EquilateralMatrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                new_matr.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return new_matr

    def __mul__(self, other):
        if self.size != other.size:
            raise ValueError("Матрицы должны быть одинакового размера.")

        new_matr = EquilateralMatrix(self.size)
        for i in range(self.size):
            for j in range(self.size):
                new_matr.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.size))
        return new_matr

    def __eq__(self, other):
        if self.size != other.size:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True


if __name__ == '__main__':
    em1 = EquilateralMatrix(3)
    em2 = EquilateralMatrix(3)
    em1.matrix = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
    em2.matrix = [[3, 2, 1], [2, 1, 3], [1, 2, 3]]
    m3 = em1 + em2
    m4 = em1 - em2
    m5 = em1 * em2
    print(m3)
    print()
    print(m4)
    print()
    print(m5)
    print(m5 == m4)
