import unittest
import ieee


class TestIEEE(unittest.TestCase):

    #ENCODER

    def test_changeWholeToBin_whole(self):
        result = ieee.changeWholeToBin(5)
        self.assertEqual(result, '101')

    #false tests

    def test_changeDecimalToBin_decimal(self):
        result = ieee.changeDecimalToBin(263.3)
        self.assertEqual(result, '55601100110011001100')
    
    #false tests 

    def test_numToBinary(self):
        result = ieee.numToBinary(263.3)
        self.assertEqual(result, '100000111.01001100110011001100')

    #false tests 

    #DECODER

    def test_getSignBit_positive(self):
        result = ieee.getSignBit('01000011010101000000000000000000')
        self.assertTrue(result)
    def test_getSignBit_negative(self):
        result = ieee.getSignBit('11000011010101000000000000000000')
        self.assertFalse(result)

    def test_getExpBit(self):
        result = ieee.getExpBit('01000011010101000000000000000000')
        self.assertEqual(result, 134)




    

# Now we can run this in bash python test_ieee.py
if __name__ == '__main__':
    unittest.main()
