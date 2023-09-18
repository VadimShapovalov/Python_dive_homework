import pytest

from triangle import triangle


def test_triangle():
    assert triangle(5, 5, 9) == 'Треугольник является равнобедренним!', 'Тест провален'


def test_triangle_type():
    assert triangle(3.5, 6, 9) == 'стороны треугольника должны быть типа int.', 'Тест провален'


def test_triangle_equal_zero():
    assert triangle(0, 6, 9) == 'Вы ввели недопустимые значения попробуйте снова!', 'Тест провален'


def test_limit():
    assert triangle(1_000_000_001, 999_999_996, 999_999_996) == 'Вы ввели недопустимые значения попробуйте снова!', 'Тест провален'


def test_negative_number():
    assert triangle(-2, 6, 9) == 'Вы ввели недопустимые значения попробуйте снова!', 'Тест провален'


if __name__ == "__main__":
    pytest.main()
