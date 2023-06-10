# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

dict_friends = {'Ivan': ('фонарь', 'спички', 'бинокль', 'веревка', 'нож', 'палатка', 'спальник', 'тушенка', 'панама'),
                'Petr': ('карта', 'зажигалка', 'панама', 'нож', 'веревка', 'репеллент', 'перчатки', 'топорик', 'кока-кола'),
                'Andrey': ('карта', 'книга', 'бейсболка', 'веревка', 'спальник', 'нож', 'бинокль', 'зажигалка', 'очки')}

for i in dict_friends.keys():
    dict_friends[i] = frozenset(dict_friends[i])
list_names = list(dict_friends.keys())

all_set = set(dict_friends[list_names[0]])
for i in range(1, len(list_names)):
    all_set = all_set & dict_friends[list_names[i]]
print(f"1. Вещи, которые есть у каждого из друзей: {list(all_set)}\n")

unicum_things = []
for i in range(len(list_names)):
    temp_set = set(dict_friends[list_names[i]])
    for j in range(len(list_names)):
        if list_names[i] != list_names[j]:
            temp_set = temp_set - dict_friends[list_names[j]]
    unicum_things.extend(temp_set)
print(f"2. Список уникальных вещей, каждая из которых есть только у одного из друзей:\n {unicum_things}\n")

for i in range(len(list_names)):
    temp_set = dict_friends[list_names[i]]
    first_set = dict_friends[list_names[i - 1]]
    for j in range(len(list_names)):
        if list_names[j] != list_names[i]:
            first_set = first_set & dict_friends[list_names[j]]
    things = first_set - temp_set
    print(f"3. Имя друга: {list_names[i]}. Предметы, которые есть у всех остальных, но нет у него: {list(things)} ")
