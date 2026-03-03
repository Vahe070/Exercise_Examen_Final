import unittest
from calculatrice import division, puissance, moyenne

class TestCalculatrice(unittest.TestCase):

    def test_division_simple(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_decimal(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    def test_puissance_normal(self):
        self.assertEqual(puissance(2, 3), 8)

    def test_puissance_zero(self):
        self.assertEqual(puissance(2, 0), 1)

    def test_puissance_negatif(self):
        with self.assertRaises(ValueError):
            puissance(2, -1)

    def test_moyenne_normal(self):
        self.assertEqual(moyenne([10, 20, 30]), 20)

    def test_moyenne_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])


if __name__ == "__main__":
    unittest.main()