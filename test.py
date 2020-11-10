import unittest
from calculator import calculator

class test(unittest.TestCase):
	
    def __init__(self):
        super().__init__()
	print("test")

    @staticmethod
    def test(self):
	    self.assertEqual(calculator.add(5,6)==11)
	    self.assertEqual(calculator.sub(15,3)==12)
	    self.assertEqual(calculator.mul(20,20)==400)
	    self.assertEqual(calculator.div(100,5)==20)
	    self.assertEqual(calculator.mod(4,6)==4)

unittest.main()
