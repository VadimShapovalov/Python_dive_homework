# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def dictionary_creation(**kwargs) -> dict:
    """function converts values to keys."""
    my_dict = dict()
    for key, val in kwargs.items():
        try:
            hash(val)
        except TypeError:
            val = str(val)
        my_dict[val] = key
    return my_dict


print(dictionary_creation(a=1, b=2, c=3, d=False, e=(4, 5), f=[6, 7], g={8, 9}, h='Hello'))
