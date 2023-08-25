# Задание №7
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку

import pickle
import csv

def convert_to_pickle_string(pickle_name:str):
    with open(pickle_name, 'r', newline='', encoding='utf-8') as f_csv:
        file = list(csv.reader(f_csv))
        str_pickle = pickle.dumps(file)
        print(str_pickle)


if __name__ == '__main__':
    convert_to_pickle_string('task6_users.csv')
