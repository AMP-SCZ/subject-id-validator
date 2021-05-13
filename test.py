import unittest
from idvalidator import validate


class TestValidation(unittest.TestCase):

    def test_good_ids(self):
        self.assertTrue(validate('ME01459'))
        self.assertTrue(validate('CA00902'))
        self.assertTrue(validate('YA00015'))
        self.assertTrue(validate('AD00017'))
        self.assertTrue(validate('SL24980'))
        self.assertTrue(validate('sl24980'))  # Same but lowercase

    def test_bad_check_digit(self):
        self.assertFalse(validate('ME01456'))  # Wrong check digit
        self.assertFalse(validate('CA09002'))  # Swapped numbers
        self.assertFalse(validate('AY00015'))  # Swapped letters
        self.assertFalse(validate('XA00015'))  # Changed letter
        self.assertFalse(validate('AD00027'))  # Changed number
        self.assertFalse(validate('SL24870'))  # Changed numbers

    def test_badly_formed_ids(self):
        self.assertFalse(validate('ME501459'))  # Too long
        self.assertFalse(validate('01459'))     # Too short
        self.assertFalse(validate('ABCDEFG'))   # All letters
        self.assertFalse(validate('ADA0011'))   # 3 letters
        self.assertFalse(validate('0000015'))   # All numbers


if __name__ == '__main__':
    unittest.main()
