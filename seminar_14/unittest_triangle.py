import unittest

from triangle import triangle


class TestTriangle(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(triangle(5, 5, 9), 'Треугольник является равнобедренним!')

    def test_triangle_type(self):
        self.assertTrue(triangle(3.5, 6, 9), 'стороны треугольника должны быть типа int.')

    def test_triangle_equal_zero(self):
        self.assertEqual(triangle(0, 6, 9), 'Вы ввели недопустимые значения попробуйте снова!')

    def test_limit(self):
        self.assertTrue(triangle(1_000_000_001, 999_999_996, 999_999_996),
                        'Вы ввели недопустимые значения попробуйте снова!')

    def test_negative_number(self):
        self.assertTrue(triangle(-2, 6, 9), 'Вы ввели недопустимые значения попробуйте снова!')


if __name__ == '__main__':
    unittest.main(verbosity=2)
