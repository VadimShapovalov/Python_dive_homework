# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

num = randint(0, 1000)
print(f"Было загадано следующее число: {num}")
low, up, count, choice = 0, 1000, 0, int
while num != choice:
    choice = (up + low) // 2
    count += 1
    if choice == num:
        print(f"Ура! Мы нашли то, что искали! Искомое число: {choice}. Потрачено попыток: {count}")
    else:
        if num > choice:
            low = choice
        else:
            up = choice
