import os
import pathlib

#print(os.listdir())

for dir_path, dir_name, file_name in os.walk(r'C:\Users\Vadim\Desktop\Dive_into_Python\Projects\Python_dive_homework\seminar_8'):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
    if dir_name > 0:


# for i in os.walk(r'C:\Users\Vadim\Desktop\Dive_into_Python\Projects\Python_dive_homework\seminar_8'):
#     print(i)
#     print(os.path.isdir(i))
#     print(os.path.isfile(i))
# size = os.path.getsize(r'C:\Users\Vadim\Desktop\Dive_into_Python\Projects\Python_dive_homework\seminar_8\task_1.py')
# print(size)