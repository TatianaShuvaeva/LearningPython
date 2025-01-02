import unittest
from operatorüberladung_bruche import Bruch


class UnitTestBruch(unittest.TestCase):

    def test_add(self):
        b1 = Bruch(1, 2)
        b2 = Bruch(1, 4)
        ergebnis = b1 + b2
        self.assertEqual(ergebnis.get_zaehler(), 3)
        self.assertEqual(ergebnis.get_nenner(), 4)

    def test_subtract(self):
        b1 = Bruch(3, 4)
        b2 = Bruch(1, 4)
        ergebnis = b1 - b2
        self.assertEqual(ergebnis.get_zaehler(), 1)
        self.assertEqual(ergebnis.get_nenner(), 2)

    def test_multiply(self):
        b1 = Bruch(2, 3)
        b2 = Bruch(3, 4)
        ergebnis = b1 * b2
        self.assertEqual(ergebnis.get_zaehler(), 1)
        self.assertEqual(ergebnis.get_nenner(), 2)

    def test_divide(self):
        b1 = Bruch(3, 5)
        b2 = Bruch(2, 3)
        ergebnis = b1 / b2
        self.assertEqual(ergebnis.get_zaehler(), 9)
        self.assertEqual(ergebnis.get_nenner(), 10)


if __name__ == '__main__':
    unittest.main()
