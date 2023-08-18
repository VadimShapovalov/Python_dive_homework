# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл

from random import randint


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


if __name__ == "__main__":
    fill_in_file_names(name_file="test_file_names", count_line=5)