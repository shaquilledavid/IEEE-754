"""
2020 PyJaC coding competition.

PyJaC is a brand-new coding competition brought to you by UTM’s Women in Science
and Computing Club (WiSC), UTM Mathematical and Computational Sciences Society
(MCSS), and UTM Physics Club (PC).

Our prompt: creat an IEEE encoder/decoder

An IEEE encoder/decoder should convert floating-point numbers to a decimal
representation and back to floating-point, depending on the operation chosen.

Project completed by: Shaquille David
                      Junayeed Rahman
                      Mohid Sharif
"""
import math

###### ENCODING FUNCTIONS

# Part 1 - Represent the number as a binary number

def changeWholeToBin(number):
    """Change a whole number to its binary representation"""
    bits = []
    last_bit = number%2
    bits.append(last_bit)

    quotient = number//2

    while quotient != 0:
        bits.append(quotient%2)
        quotient = quotient//2

    bits.reverse()
    
    return ''.join([str(elem) for elem in bits])

def changeDecimalToBin(decimal):
    """Return the first 20 bits of the decimal number to binary"""
    bits = []

    i = 0
    while i < 20:
        product = decimal * 2
        bits.append(str(product)[0])
        decimal = float('0' + str(product)[1:])
        i = i + 1

    return ''.join([str(elem) for elem in bits])
    
        
def numToBinary(num):
    """Change a number to its binary representation
    >>> numToBinary(263.3)
    '100000111.01001100110011001100'
    """
    
    if (float(num)).is_integer() == True:
        return changeWholeToBin(num)
    else:
        number_dec = num - int(num)
        number_whole = int(num)
        return changeWholeToBin(number_whole) + '.' + changeDecimalToBin(number_dec)
    
# Part 2 - Change to scientific notation
def scientific(binarynum):
    """Change a binary number to its scientific notation equivalent

    >>> scientific('100000111.01001100110011001100')
    '1.0000011101001100110011001100e8'
    """
    
    bits = []
    for i in binarynum:
        bits.append(i)

    exponent = bits.index(".") - 1 #DOUBLE CHECK THIS
    bits.remove(".")
    rest = ''.join(bits[1:])
    
    return bits[0] + '.' + rest + 'e' + str(exponent)

# Step 3 - Write the scientific notation in IEEE-754 format

