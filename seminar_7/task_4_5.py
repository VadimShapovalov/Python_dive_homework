# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randint, choice


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

EXTEN = ('.txt', '.doc', '.pdf')

def create_random_ext_files():
    ext = choice(EXTEN)
    create_files(ext=ext)

if __name__ == "__main__":
    create_files(ext='.txt')