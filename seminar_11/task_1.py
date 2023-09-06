# Добавьте ко всем задачам с семинара строки документации
# и методы вывода информации на печать.

# Задание №1
# Создайте класс МояСтрока где будут доступны все возможности str и
# дополнительно хранится имя автора строки и время создания (time.time)

from datetime import datetime


class MyString(str):
    """ class MyString with additional storage of the author's name and creation time """

    def __init__(self, value, name):
        self.name = name
        self.time = datetime.time
        self.value = value

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time = datetime.now()
        return instance

    def __str__(self):
        return f'{self.value}, {self.name}, {self.time}'


# if __name__ == '__main__':
#     ms = MyString('Good luck', 'Vadim')
#     print(ms)

# Задание №2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
# в пару списков-архивов, которые также являются свойствами экземпляра.

class Archive:
    """the Archive class contains two lists with archives of numbers and strings from previously created instances"""

    arhive_name = []
    arhive_num = []

    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __new__(cls, name, num):
        instance = super().__new__(cls)
        instance.name = name
        instance.num = num
        cls.arhive_name.append(name)
        cls.arhive_num.append(num)
        return instance

    def __str__(self):
        return f'names = {self.arhive_name}\nnumbers = {self.arhive_num}'


# if __name__ == '__main__':
#     a = Archive('Vadim', 21)
#     print(f'{a.arhive_name = }')
#     print(f'{a.arhive_num = }')
#     b = Archive('Dima', 12)
#     print(f'{b.arhive_name = }')
#     print(f'{b.arhive_num = }')

# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры,
# а не длинну и ширину. При вычитании не допускайте отрицательных значений.

class Rectangle:
    """class Rectangle with the ability to add and subtract rectangles"""

    def __init__(self, length: float, width: float = None) -> None:
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def calc_len(self):
        """method for calculating the perimeter of a rectangle."""
        return (self.width + self.length) * 2

    def calc_area(self):
        """method for calculating the area of a rectangle."""
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length=
                         (self.length + other.length),
                         width=self.width)

    def __sub__(self, other):
        return Rectangle(length=
                         abs(self.length - other.length),
                         width=self.width)

    def __eq__(self, other: "Rectangle"):
        return self.calc_area() == other.calc_area()

    def __lt__(self, other: "Rectangle"):
        return self.calc_area() < other.calc_area()

    def __gt__(self, other: "Rectangle"):
        return self.calc_area() > other.calc_area()

    def __ge__(self, other: "Rectangle"):
        return self.calc_area() >= other.calc_area()

    def __le__(self, other: "Rectangle"):
        return self.calc_area() <= other.calc_area()

    def __str__(self):
        return f'{self.length = } {self.width = }'


if __name__ == '__main__':
    r1 = Rectangle(length=2, width=2)
    print(r1)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_area() = }')

    print('---')

    r2 = Rectangle(length=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_area() = }')

    r3 = Rectangle(2, 2)
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_area() = }')
    print('---')

    r4 = Rectangle(3)
    print(f'{r4.calc_len() = }')
    print(f'{r4.calc_area() = }')

    r5 = r3 + r4

    print('---')
    print(f'{r5.calc_len() = }')
    print(f'{r5.calc_area() = }')

    print(r1 == r2)
    print(r1 <= r2)
    print(r1 >= r2)
