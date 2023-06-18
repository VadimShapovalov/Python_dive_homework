# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# функция генератор
def fib_gen(n):
    i, j = 0, 1
    for k in range(n):
        num = i + j
        i, j = j, num
        yield i

# проверка функции
for i in fib_gen(10):
    print(i)
