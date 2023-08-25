# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий.

# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }

import os
import json
import csv
import pickle

def directory_traversal(path_directory: str):
    my_dict = {}
    for dir_path, dir_name, file_name in os.walk(path_directory):
        size_d = 0
        *_, parent, name_dir = dir_path.split('\\')
        if len(file_name) > 0:
            for i in file_name:
                size_f = os.path.getsize(i)
                size_d += size_f
                my_dict[f'{dir_path}\{i}'] = {'name': i, 'parent': name_dir, 'type': 'file', 'size': size_f}
        my_dict[dir_path] = {'name': name_dir, 'parent': parent, 'type': 'dir', 'size': size_d}

    with (open('hw_f.json', 'w', encoding='utf-8') as f_json,
        open('hw_f.csv', 'w', newline='', encoding='utf-8') as f_csv,
          open('hw_f.pkl', 'wb') as f_pkl):
        json.dump(my_dict, f_json, ensure_ascii=False, indent=4)
        pickle.dump(my_dict, f_pkl)
        csv_wr = csv.writer(f_csv)
        csv_wr.writerow(['path', 'name', 'parent', 'type', 'size'])
        for key, val in my_dict.items():
            all_data = [key]
            for k, v in val.items():
                all_data.append(v)
            csv_wr.writerow(all_data)

if __name__ == '__main__':
    directory_traversal(r'C:\Users\Vadim\Desktop\Dive_into_Python\Projects\Python_dive_homework\seminar_8')



# for key, val in my_dict.items():
#     print(f'{key}:')
#     for k, v in val.items():
#         print(f'    {k}: {v}')






# for i in os.walk(r'C:\Users\Vadim\Desktop\Dive_into_Python\Projects\Python_dive_homework\seminar_8'):
#     print(i)
#     print(os.path.isdir(i))
#     print(os.path.isfile(i))
# size = os.path.getsize(r'C:\Users\Vadim\Desktop\Dive_into_Python\Projects\Python_dive_homework\seminar_8\task_1.py')
# print(size)