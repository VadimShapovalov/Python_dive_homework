# Задание №6
# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv


def pickle_to_csv (pickle_name: str, csv_name: str):
    with open(pickle_name, 'rb') as f:
        new_list = pickle.load(f, encoding='utf-8')
    with open(csv_name, 'w', newline='', encoding='utf-8') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(new_list[0].keys())
        for i in new_list:
            writer.writerow(i.values())


if __name__ == '__main__':
    pickle_to_csv('task5_users.pickle', 'task6_users.csv')