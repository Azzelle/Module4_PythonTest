import math

def test_check():
    num = 100
    assert (num >= 100) == True

def test_sqrt():
    number = 9
    assert math.sqrt(number) == 3

def test_square():
    num = 7
    assert 7*7 == 49




# def check(num):
#     return num >= 100

# class TestGreater(unittest.TestCase):

#     def test(self):
#         self.assertTrue(check(99))

# if __name__ == '__main__':
#     unittest.main()
    