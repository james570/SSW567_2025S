import unittest
import pytest
from classify_triangle import classify_triangle  # 引用你的 classify_triangle 函數

class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
        self.assertEqual(classify_triangle(5, 8, 5), "Isosceles")
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")
    def test_scalene(self):
        self.assertEqual(classify_triangle(7, 10, 5), "Scalene")
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right Triangle")
    def test_invalid_input(self):
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid input: Side lengths must be positive")
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid input: Side lengths must be positive")
        self.assertEqual(classify_triangle("a", 4, 5), "Invalid input: Side lengths must be numbers")
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Invalid input: Not a valid triangle")
        self.assertEqual(classify_triangle(10, 1, 1), "Invalid input: Not a valid triangle")

@pytest.mark.parametrize("a, b, c, expected", [
    (5, 5, 5, "Equilateral"),
    (5, 5, 8, "Isosceles"),
    (7, 10, 5, "Scalene"),
    (3, 4, 5, "Scalene and Right Triangle"),
    (-3, 4, 5, "Invalid input: Side lengths must be positive"),
    (1, 2, 3, "Invalid input: Not a valid triangle")
])

def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
