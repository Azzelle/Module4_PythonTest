import unittest

def check(num):
    return num >= 100

class TestGreater(unittest.TestCase):

    def test(self):
        self.assertTrue(check(99))

if __name__ == '__main__':
    unittest.main()