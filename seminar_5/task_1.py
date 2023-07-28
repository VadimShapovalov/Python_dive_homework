# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def string_split(text):
    *path, filename = text.split("\\")
    name, extension = filename.split(".")
    return "\\".join(path), name, extension


line = "C:\\Users\\Vadim\\Downloads\\file.txt"
print(string_split(line))
