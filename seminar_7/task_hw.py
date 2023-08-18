# Урок 7. Файлы и файловая система
# Решить задачи, которые не успели решить на семинаре.
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

import os


def renamed_group_files(dir:str ,end_file_name:str , numbers_of_name:int ,  extension_file:str ,
                        end_extension_file:str , diapazon:list[int]) -> None:
    if not os.path.exists(dir):
        raise Exception('Dir not found')
    os.chdir(dir)
    count = 1
    for file in os.listdir():
        if os.path.isfile(file):
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
                    os.replace(file_name + '.' + extension , result_name)
                    count += 1
            except Exception as e:
                continue

renamed_group_files('test','endFile',2,'txt','csv',[1,4])