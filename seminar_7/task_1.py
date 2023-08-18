# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def fill_in_file(count_f: int, file_name: str):
    with open(file_name + '.txt', 'a', encoding='utf-8') as f:
        for _ in range(count_f):
            f.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)}\n')


if __name__ == '__main__':
    fill_in_file(5, 'test_file_numbers')
