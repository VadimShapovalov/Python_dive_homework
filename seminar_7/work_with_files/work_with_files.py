# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform, choice
from os import getcwd, listdir, mkdir, path, replace, getcwd, chdir
from pathlib import Path

EXTEN = ('.txt', '.doc', '.pdf')

def fill_in_file(count_f: int, file_name: str):
    with open(file_name + '.txt', 'a', encoding='utf-8') as f:
        for _ in range(count_f):
            f.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)}\n')



# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл


def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def fill_in_file_names(name_file: str, count_line: int) -> None:
    name_file += '.txt'

    with open(name_file, 'a', encoding='utf-8') as file:
        for _ in range(count_line):
            file.write(f"{give_name()}\n")

# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def read_and_write_files(name_file_names: str,
                        name_file_numbers: str,
                        name_file_output: str) -> None:
    with (open(name_file_names, 'r', encoding='utf-8') as file_names,
        open(name_file_numbers, 'r', encoding='utf-8') as file_numbers):
        names = file_names.read().split('\n')
        numbers = file_numbers.read().split('\n')
        if len(numbers) > len(names):
            names += names[:len(numbers)-len(names)]
        else:
            numbers += numbers[:len(names)-len(numbers)]
    with (open(name_file_output, 'w', encoding='utf-8') as file_output):
        for name, number in zip(names, numbers):
            if not name or not number:
                break

            number_output_int, number_output_float = map(float, number.split(' | '))

            multik: float = number_output_int * number_output_float

            if multik < 0:
                file_output.write(f"{name.lower()} {abs(multik)} \n")
            else:
                file_output.write(f"{name.upper()} {int(multik)} \n")


# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.



def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, min_len: int = 6,
    max_len: int = 30, min_size: int = 256,
    max_size: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        with(open(give_name() + ext, 'w', encoding='utf-8') as file_output):
            list_of_bytes = bytes([randint(0,255) for x in range(min_size, max_size)])

            file_output.write(str(list_of_bytes))



def create_random_ext_files():
    ext = choice(EXTEN)
    create_files(ext=ext)


# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, directory: str = None, min_len: int = 6,
                max_len: int = 30, min_size: int = 256,
                max_size: int = 4096, count_files: int = 42):
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
            directory = getcwd() + '\\' + directory + '\\'

    for _ in range(count_files):
        with open(directory + give_name() + ext, 'w',
                encoding='utf-8') as output:
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size, max_size)])

            output.write(str(list_of_bytes))



# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы,
# которые не подошли для сортировки.


def sort_files(directory: str | Path = 'test_dir'):
    chdir(directory)
    print(listdir())
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        file.replace(f"{ext.upper()}\\{file.name}")


# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый
# номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
# внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#   old_file.dat ->'endFile' , '*.ext'  2 [2,5] ->  ld_fendFile01.ext


def renamed_group_files(dir:str ,end_file_name:str , numbers_of_name:int ,  extension_file:str ,
                        end_extension_file:str , diapazon:list[int]) -> None:
    if not path.exists(dir):
        raise Exception('Dir not found')
    chdir(dir)
    count = 1
    for file in listdir():
        if path.isfile(file):
            try:
                file_name , extension = file.split('.')[0] , file.split('.')[1]
                if extension == extension_file:
                    if len(file_name) < diapazon[0]:
                         file_replece = file_name
                    elif len(file_name) < diapazon[1]:
                        file_replece = file_name[diapazon[0]:]
                    else:
                        file_replece = file_name[diapazon[0]:diapazon[1]]
                    if len(str(count)) < numbers_of_name:
                        str_number = '0'*(numbers_of_name - len(str(count))) + str(count)
                    else:
                        str_number = str(count)

                    result_name = file_replece + end_file_name + str_number + '.' + end_extension_file
                    replace(file_name + '.' + extension , result_name)
                    count += 1
            except Exception as e:
                continue