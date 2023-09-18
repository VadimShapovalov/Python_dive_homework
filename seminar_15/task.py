'''
Второе задание
📌 Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
    Также реализуйте возможность запуска из командной строки с передачей параметров.
'''
import logging
import sys
import argparse

logging.basicConfig(filename='task_2.log', level=logging.ERROR, encoding='utf-8')

class SideError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        logging.error(f'Значение должно быть положительное. Вы пытаетесь установить: {self.value}')
        return f'Значение должно быть положительное. Вы пытаетесь установить: {self.value}'

class Rectangle:

    def __init__(self, length: int, width: int = None):
        if length > 0:
            self.length = length
        else:
            raise SideError(length)
        if width is not None and width > 0:
            self.width = width
        elif width is None:
            self.width = length
        else:
            raise SideError(width)


    def perimeter(self):
        ''' Perimeter'''
        return (self.length + self.width) * 2

    def square(self):
        ''' Square'''
        return self.length * self.width

    def __doc__(self):
        return "Документация"

    def __add__(self, other):
        ''' сложения'''
        return self.perimeter() + other.perimeter()

    def __sub__(self, other):
        ''' вычитания '''
        return abs(self.perimeter() - other.perimeter())

    def __eq__(self, other):
        ''' сравнения'''
        return self.square() == other.square()

    def __ne__(self, other):
        ''' сравнения'''
        return self.square() != other.square()

    def __gt__(self, other):
        ''' сравнения'''
        return self.square() > other.square()

    def __ge__(self, other):
        ''' сравнения'''
        return self.square() >= other.square()

    def __lt__(self, other):
        ''' сравнения'''
        return self.square() < other.square()

    def __le__(self, other):
        ''' сравнения'''
        return self.square() <= other.square()

    def __str__(self):
        return f'Длина - {self.length}, Ширина - {self.width}'

    def __repr__(self):
        return f'Длина - {self.length}, Ширина - {self.width}'

class MatrixError(Exception):
    def __init__(self, matrix, other):
        self.col = len(matrix)
        self.row = len(matrix[0])
        self.col1 = len(other)
        self.row1 = len(other[0])

    def __str__(self):
        logging.error(f'Матрицы разных размеров. Кол-во столбцов 1- {self.col} 2- {self.col1}. Кол-во строк 1- {self.row} 2- {self.row1}')
        return f'Матрицы разных размеров. Кол-во столбцов 1- {self.col} 2- {self.col1}. Кол-во строк 1- {self.row} 2- {self.row1}'

class Matrix:
    '''
    Задание

    📌 Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
    📌 Создайте класс Матрица. Добавьте методы для:
        ○ вывода на печать,
        ○ сравнения,
        ○ сложения,
        ○ *умножения матриц
    '''

    def __init__(self, matrix: list[list[int]]):
        ''' Инициализация '''
        self.matrix = matrix

    def matrix_transposition(self):
        '''
        функция для транспонирования матрицы
        '''
        new_matrix = [[0] * len(self.matrix) for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                new_matrix[j][i] = self.matrix[i][j]
        return new_matrix


    def __str__(self):
        ''' Вывод матрицы '''
        res = 'Вывод для пользователя: \n'
        for row in self.matrix:
            for elem in row:
                res += ''.join(f'{elem}\t')
            res += ''.join('\n')
        return res

    def __repr__(self):
        ''' Вывод матрицы '''
        res = 'Вывод для разработчика: \n'
        for row in self.matrix:
            for elem in row:
                res += ''.join(f'{elem}\t')
            res += ''.join('\n')
        return res

    def sum_matrix(self):
        ''' Сумма всех элементов матрицы'''
        res = 0
        for row in self.matrix:
            for elem in row:
                res += elem
        return res

    def __add__(self, other):
        ''' Метод сложения'''
        res = []
        row = []
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                res.append(row)
                row = []
            return Matrix(res)
        else:
            raise MatrixError(self.matrix, other.matrix)


    def __mul__(self, other):
        ''' Метод умножения'''
        res = []
        row = []
        if len(self.matrix) == len(other.matrix[0]) and  len(other.matrix) == len(self.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] * other.matrix[j][i])
                res.append(row)
                row = []
            return Matrix(res)
        else:
            raise MatrixError(self.matrix, other.matrix)


    ''' Методы сравнения'''
    def __eq__(self, other):
        return self.sum_matrix() == other.sum_matrix()

    def __ne__(self, other):
        return self.sum_matrix() != other.sum_matrix()

    def __gt__(self, other):
        return self.sum_matrix() > other.sum_matrix()

    def __ge__(self, other):
        return self.sum_matrix() >= other.sum_matrix()

    def __lt__(self, other):
        return self.sum_matrix() < other.sum_matrix()

    def __le__(self, other):
        return self.sum_matrix() <= other.sum_matrix()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='прямоугольник')
    parser.add_argument('-a', metavar='a', type=float, help='enter a for Rectangle', default=1)
    parser.add_argument('-b', metavar='b', type=float, help='enter b for Rectangle')
    args = parser.parse_args()
    print(Rectangle(args.a, args.b))
    # примеры вывода
    # python3 HW_Task_02.py -a 2 -b 3
    # python3 HW_Task_02.py -a 2

    # parser = argparse.ArgumentParser(description='Матрица')
    # parser.add_argument('-a', metavar='a', type=list[list[int]], help='enter a for Matrix', default=[[1, 1], [1, 1]])
    # parser.add_argument('-b', metavar='b', type=list[list[int]], help='enter b for Matrix', default=[[1, 1], [1, 1]])
    # args = parser.parse_args()
    # matrix = Matrix(args.a)
    # matrix_1 = Matrix(args.b)
    # print(matrix.sum_matrix())
    # print(matrix * matrix_1)
