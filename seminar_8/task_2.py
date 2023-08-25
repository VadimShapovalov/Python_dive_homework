# Задание №2

# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.

# {
#     level: {
#         id: name,
#         ...
#     },
#     ...
# }

import json


def enter_id_name(name_file: str) -> None:
    name_file += ".json"

    while True:
        id = input("id: ")
        name = input("name: ")
        level = input("level: ")

        try:
            with open(name_file, 'r', encoding='utf-8') as fr:
                read_dict: dict = json.load(fr)

        except:
            read_dict: dict = {str(i): {} for i in range(1, 8, 1)}

        read_dict[level].update({id: name})

        with open(name_file, 'w', encoding='utf-8') as fw:
            json.dump(read_dict, fw, indent=2)


if __name__ == "__main__":
    enter_id_name(name_file='users')

