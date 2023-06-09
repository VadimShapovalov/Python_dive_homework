# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hex_convertor():
    print("Введите целое десятичное число: ")
    num_ten = int(input())
    # num_ten = 10000
    num_from_hex = hex(num_ten)
    num_hex = ''
    while num_ten > 0:
        digit = num_ten % 16
        if 0 < digit < 10: num_hex = str(digit) + num_hex
        num_ten //= 16
        match digit:
            case 10:
                num_hex = 'A' + num_hex
            case 11:
                num_hex = 'B' + num_hex
            case 12:
                num_hex = 'C' + num_hex
            case 13:
                num_hex = 'D' + num_hex
            case 14:
                num_hex = 'E' + num_hex
            case 15:
                num_hex = 'F' + num_hex
            case 0:
                num_hex = '0' + num_hex
    return f"Число полученное нашим конвертором: 0x{num_hex}\nЧисло полученное функцией hex:{num_from_hex}"

print(hex_convertor())
