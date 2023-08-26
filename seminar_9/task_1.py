# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from random import randint


def generation_csv(filename: str):  # '100_nums.csv'
    with open(filename, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        for i in range(randint(100, 1000)):
            writer.writerow([randint(1, 50), randint(15, 100), randint(1, 50)])


generation_csv('100_nums.csv')


def start_func_with_csv(func):
    with open('100_nums.csv', 'r', newline='') as r_csv:
        my_dict = {}
        rows = list(csv.reader(r_csv))
    def wrapper(*args):
        for i in rows:
            my_dict[str(i)] = func(int(i[0]), int(i[1]), int(i[2]))
        return my_dict
    return wrapper


def save_to_json(func):
    def wrapper(*args):
        my_dict = func()
        with open('save_square_roots.json', 'w', encoding='utf-8') as f:
            json.dump(my_dict, f, indent=4)
        return my_dict
    return wrapper


@save_to_json
@start_func_with_csv
def find_square_root(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    return x1, x2


find_square_root()
