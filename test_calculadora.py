import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):
    def test_2_mas_2(self):
        calc = calculadora()
        self.assertEqual(4, calc.sumar(2, 2))
    def test_10_mas_2(self):
        calc = calculadora()
        self.assertEqual(11, calc.sumar(10, 2))

if __name__ == '__main__':
    unittest.main()