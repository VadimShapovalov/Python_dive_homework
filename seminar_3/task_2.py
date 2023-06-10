# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 3, 5, 3, 7, 9, 12, 21, 12, 21, 8, 7, 6, 3, 24, 24, 42, 24, 47, 42, 33, 47]

def duplicates(my_list: list) -> list:
    result_set = set()
    for i in my_list:
        if my_list.count(i) > 1:
            result_set.add(i)
    res_list = list(result_set)
    return res_list

print(duplicates(my_list))
