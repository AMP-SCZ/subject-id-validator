import unittest
from idvalidator import validate


class TestValidation(unittest.TestCase):

    def test_good_ids(self):
        self.assertTrue(validate('ME01459'))
        self.assertTrue(validate('me01459'))  # Same but lowercase
        self.assertTrue(validate('CA00902'))
        self.assertTrue(validate('Ca00902'))  # Same but w/ lowercase
        self.assertTrue(validate('BM26622'))
        self.assertTrue(validate('bM26622'))  # Same but w/ lowercase
        self.assertTrue(validate('BM43632'))
        self.assertTrue(validate('YA00015'))
        self.assertTrue(validate('YA93169'))
        self.assertTrue(validate('AD77511'))
        self.assertTrue(validate('SL24980'))
        self.assertTrue(validate('NN12344'))
        self.assertTrue(validate('NN56786'))
        self.assertTrue(validate('NN98764'))

    def test_bad_check_digit(self):
        # See README.md for check digit algorithm
        self.assertFalse(validate('ME01456'))  # ME01459 Wrong check digit
        self.assertFalse(validate('CA09002'))  # CA00902 Swapped numbers
        self.assertFalse(validate('BM22662'))  # BM26622 Swapped numbers
        self.assertFalse(validate('BM46332'))  # BM43632 Swapped numbers
        self.assertFalse(validate('AY00015'))  # YA00015 Swapped letters
        self.assertFalse(validate('XA93169'))  # YA93169 Changed letter
        self.assertFalse(validate('AD77521'))  # AD77511 Changed number
        self.assertFalse(validate('SL24870'))  # SL24980 Changed numbers

    def test_badly_formed_ids(self):
        # A well-formed ID is 7 characters long, consisting of two
        # letters followed by four digits
        self.assertFalse(validate('ME501459'))  # Too long
        self.assertFalse(validate('01459'))     # Too short
        self.assertFalse(validate('ABCDEFG'))   # All letters
        self.assertFalse(validate('ADA0011'))   # 3 letters
        self.assertFalse(validate('0000015'))   # All numbers


if __name__ == '__main__':
    unittest.main()
