import leapyear
import unittest

class testLeapYear(unittest.TestCase):
    def test_leapyear1(self):
        result = leapyear.main(2000)
        self.assertEqual(result, True)

    def test_leapyear2(self):
        result = leapyear.main(1900)
        self.assertEqual(result, False)

    def test_leapyear3(self):
        result = leapyear.main(2021)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main(verbosity=2)