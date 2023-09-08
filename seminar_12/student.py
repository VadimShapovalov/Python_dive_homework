# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from copy import copy
import pickle

class Desc:
    """Дескриптор для проверки ФИО на наличие только букв и на первую заглавную букву."""

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value: str):
        if not (value.isalpha() and value.istitle()):
            raise ValueError('ФИО должны содержать только буквы и начитаться с заглавной буквы')

class Student:
    """Класс Студент с возможностью хранения оценок и результатов тестов."""
    name = Desc()
    surname = Desc()
    patronymic = Desc()

    def __init__(self, surname, name, patronymic):
        """Переопределил метод так, чтобы он проверял, были ли в архиве студент с таким ФИО."""
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.fio = f'{self.name} {self.surname} {self.patronymic}'
        with open('subjects.csv', 'r', encoding='utf-8', newline='') as f:
            di = csv.reader(f)
            self.dict_test = dict.fromkeys(*di, None)
            self.dict_grade = copy(self.dict_test)
        try:
            with open('arhiv.pkl', 'rb') as arh:
                list_a = list(pickle.load(arh))
            for i in list_a:
                if i.fio == self.fio:
                    self.surname = i.surname
                    self.name = i.name
                    self.patronymic =i.patronymic
                    self.dict_test = i.dict_test
                    self.dict_grade = i.dict_grade
        except EOFError:
            pass

    def __str__(self):
        return f'{self.fio}\nОценки: {self.dict_grade}\nТесты: {self.dict_test}'

    def average_grade(self):
        """Метод выводит среднюю оценку студента по всем предметам."""
        av = 0
        count = 0
        for i in self.dict_grade.values():
            if i !=None:
                for j in i:
                    av += j
                    count +=1
        try:
            av = av / count
            print(f'{self.fio}: cредняя оценка  по всем предметам - {av:.2f}')
        except ZeroDivisionError:
            print('В базе еще нет оценок у данного студента.')

    def average_subject(self, subject):
        """Метод выводит средний балл за тесты по конкретному предмету."""
        if subject in self.dict_test.keys():
            if self.dict_test[subject] is None:
                print('По данному предмету тестов не проводилось.')
            else:
                sum_ = 0
                for i in self.dict_test[subject]:
                    sum_ += i
                av = sum_ / len(self.dict_test[subject])
                print(f'{self.fio}: cредний результат тестирования по предмету "{subject}" - {av:.2f}')

    def enter_test(self):
        """Метод для внесения результатов тестов. Он же сериализует данные в архиве."""
        print('Выберите название предмета из списка:\nматематика\nлитература\nхимия\nистория\nфизика')
        sub = input()
        if sub not in self.dict_test.keys():
            raise ValueError('Будьте внимательны! Вы некорректно ввели название предмета. Повторите попытку.')
        print('Введите результаты теста:')
        try:
            res = int(input())
        except ValueError:
            print('Результатом теста может быть только число от 0 до 100.')
        if -1 < res < 101:

            if self.dict_test[sub] == None:
                self.dict_test[sub] = [res]
            else:
                self.dict_test[sub].append(res)
        else:
            print('Результатом теста может быть только число от 0 до 100.')
            raise ValueError('Повторите попытку записи результатов')
        try:
            with open('arhiv.pkl', 'rb') as arh:
                list_a = list(pickle.load(arh))
            for i in list_a:
                if i.fio == self.fio:
                    list_a.remove(i)
            list_a.append(self)
        except EOFError:
            list_a = [self]
        with open('arhiv.pkl', 'wb') as ar:
            pickle.dump(list_a, ar)

    def enter_grade(self):
        """Метод для внесения оценок и сохранения в архиве."""
        print('Выберите название предмета из списка:\nматематика\nлитература\nхимия\nистория\nфизика')
        sub = input()
        if sub not in self.dict_grade.keys():
            raise ValueError('Будьте внимательны! Вы некорректно ввели название предмета. Повторите попытку.')
        print('Введите оценку:')
        try:
            res = int(input())
        except ValueError:
            print('Оценка может быть в диапазоне от 2 до 5.')
        if 1 < res < 6:
            if self.dict_grade[sub] == None:
                self.dict_grade[sub] = [res]
            else:
                self.dict_grade[sub].append(res)
        else:
            print('Оценка может быть в диапазоне от 2 до 5.')
            raise ValueError('Повторите попытку записи результатов')
        try:
            with open('arhiv.pkl', 'rb') as arh:
                list_a = list(pickle.load(arh))
            for i in list_a:
                if i.fio == self.fio:
                    list_a.remove(i)
            list_a.append(self)
        except EOFError:
            list_a = [self]
        with open('arhiv.pkl', 'wb') as ar:
            pickle.dump(list_a, ar)

if __name__ == '__main__':

    vadim = Student('Shapovalov', 'Vadim', 'Vladimirovich')
    # vadim.average_grade()
    vadim.average_subject('математика')
    vadim.average_grade()
    # vadim.enter_test()
    ivan = Student('Ivanov', 'Ivan', 'Ivanich')
    ivan.average_subject('физика')
    ivan.average_grade()
    # ivan.enter_test()
    # ivan.enter_grade()
    print(vadim)
    print(ivan)
