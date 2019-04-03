#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


# ```````` helper functions for decode ```````` #

# digit string to digits, base = 10
def digit(digits):
    return int(digits)

# binary to digits, base = 2
def binaryToDigits(digits):
    mult = 0 # the exponential power for 2
    result = 0

    for i in range(len(digits)-1, -1, -1): # loop in reverse
        if (digits[i] == ' '):
            continue
        temp = 0 # what binary digit we are on, 1 or 0
        if (digits[i] == '1'):
            temp = 1

        result += (2**mult)*temp
        mult += 1
    
    return result

# hexadecimal to digits, base = 16
def hexToDigits(digits):
    # if digit: use that as temp
    # if letter: 10 + (ord('letter') - ord('A'))
    mult = 0
    result = 0
    
    for i in range(len(digits)-1, -1, -1): # loop in reverse
        curr = digits[i]
        # print("curr:%s"%curr)
        temp = 0 # value for current hex bit
        # print("temp:%d"%temp)
        if (curr == ' '): # if space
            continue
        elif (curr.lower() == 'x'): # if marker for hex, but not part of hex num
            break
        elif (curr.isdigit()): # if number
            temp = int(curr)
        elif (curr.isalpha()): # if letter
            curr = curr.lower()
            temp = 10 + (ord(curr) - ord('a')) # get its value
        
        result += (16**mult)*temp
        # print(result, mult, temp)
        mult += 1
    
    return result

# all bases
def convertToDigits(digits, base):
    mult = 0 # exponent power for base
    result = 0
    
    for i in range(len(digits)-1, -1, -1): # loop in reverse
        curr = digits[i]
        # print(curr)
        temp = 0 # value for current hex bit
        if (curr == ' '): # if space
            continue
        # elif (curr.lower() == 'x'): # if marker for hex, but not part of hex num
        #     break
        temp = string.printable.index(curr)
        # temp = 10 + (ord(curr) - ord('a'))
        result += (base**mult)*temp
        mult += 1
    
    return result


# ```````` helper functions for encode ```````` #
def getBinaryLength(digits, i):
    exp = int(math.log(digits, i))
    # make sure exp is valid 
    if (i == 2 and (exp+1)%4 != 0):
        if ((exp+2)%4 == 0):
            exp += 1
        elif ((exp-2)%4 == 0):
            exp -= 1
    return exp
# input is an integer, convert it to base 2
def digitToBinary(digit):
    result = ""
    # to get the len for binary and max exp value for 2, do log base 2 of digit
    # use that as the start value
    exp = getBinaryLength(digit, 2)
    # grammar, spacing
    # count = 0
    while (exp >= 0):
        # formatting
        # if (count == 4):
        #     count = 0
        #     result += ' '
        
        # 2's exponential value for this bit
        temp = 2**exp
        exp -= 1
        if (digit >= temp):
            digit -= temp
            result += '1'
        else:
            result += '0'
        # count += 1
    return result

# digit to hexadecimal, base 16
def digitToHex(digit):
    result = ""
    hexvals = string.hexdigits
    print(hexvals)
    while (digit > 0):
        rem = int(digit % 16)
        print(rem)
        # remainder is the hex digit
        result = hexvals[rem] + result

        digit //= 16
        print("DIGIT: %d"%digit)
        print(digit > 0)
    return result

# converts a digit to any base specified
def digitToBase(digit, base):
    # digit = int(digit)
    result = ""
    # print(hexvals)
    while (digit > 0):
        rem = int(digit % base) # the hex digit
        result = string.printable[rem] + result
        digit //= base
    return result

# ```````` helper functions for convert ```````` #

# Convert digits from base 2 to base 16 (and vice versa)
def convert2and16(digits, base):
    result = ""
    digits = digits.lower()
    if base == 16:
        # evaluate binary for each hex bit
        for dig in digits:
            temp = 0
            if (dig.digit()):
                temp = int(dig)
            if (dig.isalpha()):
                temp = 10 + (ord(dig) - ord('a')) # get its value
            result += encode(temp, 2)
    if base == 2:
        # make sure length is in 4's to convert each set of 4 to binary
        while (len(digits)%4 != 0):
            digits = '0' + digits
        # print(digits)

        for i in range(0, len(digits), 4):
            digit10 = decode(digits[i:i+4], 2) # base 10
            result += encode(digit10, 16)
    return result.lower()


# ```````` ASSIGNED: DECODE AND ENCODE FUNCTIONS ```````` #

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2) --> binaryToDigits(digits)
    # Decode digits from hexadecimal (base 16)--> hexToDigits(digits)
    # Decode digits from any base (2 up to 36) --> convertToDigits(digits, base)
    mult = 0 # exponent power for base
    result = 0
    
    for i in range(len(digits)-1, -1, -1): # loop in reverse
        curr = digits[i]
        val = 0 # value for current bit
        if (curr == ' '): # if space formatting
            continue
        # elif (curr.lower() == 'x'): # if marker for hex, but not part of hex num
        #     break
        # val = string.printable.index(curr) # value for that individual bit --> slower
        val = 0 
        if (curr.isalpha()): 
            val = 10 + (ord(curr) - ord('a')) # faster than using .index()
        elif (curr.isdigit()):
            val =int(curr)
        result += (base**mult)*val # value for that bit in its location
        mult += 1
    
    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # Encode number in binary (base 2) ---> digitToBinary(number)
    # Encode number in hexadecimal (base 16) ---> digitToHex(number)
    # Encode number in any base (2 up to 36) ---> digitToBase(int(number), base).lower()
    digit = int(number)
    result = ""
    # print(hexvals)
    while (digit > 0):
        rem = int(digit % base) # the hex digit
        result = string.printable[rem] + result
        digit //= base
    
    return result


# ```````` ASSIGNED: CONVERT FUNCTION ```````` #

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Convert digits from base 2 to base 10 (and vice versa)
    # Convert digits from base 10 to base 16 (and vice versa)
    # if (base2 == 10): --> str(decode(digits, base1))
    # if (base1 == 10): --> encode(int(digits), base2).lower()
    # Convert digits from base 2 to base 16 (and vice versa) --> return convert2and16(digits, base1)
    # Convert digits from any base to any base (2 up to 36)
    digit10 = decode(digits, base1)
    return encode(digit10, base2).lower()

# ```````` STRETCH CHALLENGES ```````` #

# ```` helpers ````

# inverts bits for given binary --> 0's = 1's and 1's = 0's
def invertBits(digits):
    invertedBit = ''
    for digit in digits:
        if (digit == '1'):
            invertedBit += '0'
        elif (digit == '0'):
            invertedBit += '1'
    return invertedBit

# adds 1 to given binary
def addOneToBinary(digits):
    carry = '1'
    result = ''
    for i in range(len(digits)-1, -1, -1):
        curr = digits[i]
        if (curr == '1' and carry == '1'):
            result += '0'
        elif (curr == '0' and carry == '1'):
            result += '1'
            carry = '0'
        elif (curr == '1' and carry == '0'):
            result += '1'
        elif (curr == '0' and carry == '0'):
            result += '0'
    return result

# ````````  base conversion for negative binary numbers (using two's complement, base 2) ```````` #
def twosComplementToDigit(digits):
    if (digits[0] == '1'): # if negative number: invert and add one
        modifiedDigits = ''.join(reversed(addOneToBinary(invertBits(digits))))
        return -1*decode(modifiedDigits, 2)
    
    return decode(digits, 2) # positive number

# works for 8 bit only
def digitToTwosComplement(digit):
    if (digit < 0): 
        # convert to binary
        unsignedDigits = encode(abs(digit), 2)
        # negate by inverting and adding 1
        modifiedDigits = addOneToBinary(invertBits(unsignedDigits))
        return '1'+ ''.join(reversed(modifiedDigits))

    return encode(digit, 2)

# ```````` base conversion for fractional numbers using a radix point ```````` #

# helper for digit to fractional binary function
def encodeDecimal(digit):
    result = ""
    # print(hexvals)
    while (digit > 0):
        temp = digit*2
        result += str(int(temp))
        digit = temp - int(temp)
    
    return result

def digitToFractionalBinary(digit):
    return encode(int(digit), 2) + '.' + encodeDecimal(digit - int(digit))



# helper for fractional binary to digit function
def decodeDecimal(digits):
    mult = -1 # exponent power for base
    result = 0
    
    for curr in digits: # loop in reverse
        val = 0 # value for current bit
        if (curr == ' '): # if space formatting
            continue
        val = int(curr)
        result += (2**mult)*val # value for that bit in its location
        mult -= 1
    
    return result

# base 2 fractional binery to base 10 digit
def fractionalBinaryToDigit(digits):
    arr = digits.split('.')
    if (len(arr) <= 1):
        return decode(digits, 2)
    
    wholenum = decode(arr[0], 2)

    decimalnum = decodeDecimal(arr[1])

    return wholenum + decimalnum



def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    print("TESTING STRETCH CHALLENGES")
    print(fractionalBinaryToDigit('1101.101')) # 13.625
    print(digitToFractionalBinary(13.625))

