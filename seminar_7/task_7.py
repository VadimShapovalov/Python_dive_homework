

from os import chdir, listdir, mkdir, getcwd
from pathlib import Path

# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы,
# которые не подошли для сортировки.


def sort_files(directory: str | Path = 'test_dir_1'):
    chdir(directory)
    print(listdir())
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        file.replace(f"{ext.upper()}\\{file.name}")

