# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

text = "C:\\Users\\Vadim\\Downloads\\file.txt"


def string_split(text):
    *path, filename = text.split("\\")
    name, extension = filename.split(".")
    return "\\".join(path), name, extension


print(string_split(text))
