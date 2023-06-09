# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions
import math

def sum_mult_fractions():
    fraction_1 = input("Введите первую дробь в формате 1/2: ")
    fraction_2 = input("Введите вторую дробь в формате 1/2: ")
    numerator, denominator = fraction_1.split("/")
    numerator_2, denominator_2 = fraction_2.split("/")
    int_numerator, int_denominator = int(numerator), int(denominator)
    int_numerator_2, int_denominator_2 = int(numerator_2), int(denominator_2)
    lcm = (int_denominator * int_denominator_2) // math.gcd(int_denominator, int_denominator_2)
    multiple_1, multiple_2 = lcm // int_denominator, lcm // int_denominator_2
    new_numerator_1, new_numerator_2 = int_numerator * multiple_1, int_numerator_2 * multiple_2
    print(f"Сумма дробей равна {new_numerator_1 + new_numerator_2}/{lcm}")
    mult_numerator, mult_denominator = int_numerator * int_numerator_2, int_denominator * int_denominator_2
    gcd = math.gcd(mult_numerator, mult_denominator)
    print(f"Произведение дробей равно: {mult_numerator // gcd}/{mult_denominator // gcd}")
    fract_1 = fractions.Fraction(int(numerator), int(denominator))
    fract_2 = fractions.Fraction(int(numerator_2), int(denominator_2))
    print(f"Сумма дробей полученная путем модуля fructions: {fract_1 + fract_2}")
    print(f"Произведение дробей полученное путем модуля fructions: {fract_1 * fract_2}")

sum_mult_fractions()

