import unittest
import utils

class TestStringMethods(unittest.TestCase):
    def test_reversed_string(self):
        with self.assertRaises(Exception) as context:
            utils.reversed('12345')
        self.assertEqual(str(context.exception), 'Input is not an Integer')

    def test_reversed_float(self):
        with self.assertRaises(Exception) as context:
            utils.reversed(12.345)
        self.assertEqual(str(context.exception), 'Input is not an Integer')
    
    def test_reversed_integer(self):
        self.assertEqual(utils.reversed(12345), 54321)
    
    def test_formatter_string(self):
        with self.assertRaises(Exception) as context:
            utils.formatter('12345')
        self.assertEqual(str(context.exception), 'Input is not an Integer')


    def test_formatter_float(self):
        with self.assertRaises(Exception) as context:
            utils.formatter(12.345)
        self.assertEqual(str(context.exception), 'Input is not an Integer')

    def test_formatter_integer(self):
        self.assertEqual(utils.formatter(12345)[0], '0b11000000111001')
        self.assertEqual(utils.formatter(12345)[1], '0o30071')

if __name__ == '__main__':
    unittest.main()