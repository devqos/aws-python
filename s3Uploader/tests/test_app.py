import unittest


class TestApp(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(2 + 2, 4)

    def test_subtract_two_numbers(self):
        self.assertEqual(2 - 2, 0)

    if __name__ == '__main__':
        unittest.main()
