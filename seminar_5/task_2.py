# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Vasya", "Petya", "Ira", "Anna"]
salary = [100000, 230000, 60000, 310000]
bonus = ['10.25%', '15.4%', '12.2%', '8.5%']

# однострочный генератор словаря
my_dict = {i[0]: i[1] / 100 * float(i[2][:-1]) for i in zip(names, salary, bonus)}

# проверка генератора
print(my_dict)

