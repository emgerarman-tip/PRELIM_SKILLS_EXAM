import unittest
from temperature import Temperature

class TestTemperature (unittest.TestCase):

    def test_kelvin (self):
        self.assertEqual(Temperature(2).kelvin, 2)

    def test_celsius (self):
        celsius_test = 3 + 273.15
        temp = Temperature(celsius=3)
        self.assertEqual(temp.kelvin, 276.15)

    def test_fahrenheit (self):
        fahrenheit_test = (5 - 32) *5/9 + 273.15
        temp = Temperature(fahrenheit=5)
        self.assertEqual(temp.kelvin, fahrenheit_test)

    def test_input1 (self):
        self.assertRaises(ValueError, Temperature, -1)

    def test_input2 (self):
        self.assertRaises(ValueError, Temperature, None)

    def test_input3 (self):
        arguments = (2, 3, 5)
        self.assertRaises(ValueError, Temperature, *arguments)