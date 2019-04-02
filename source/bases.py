#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# helper functions

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
        print(curr)
        temp = 0 # value for current hex bit
        if (curr == ' '): # if space
            continue
        elif (curr.lower() == 'x'): # if marker for hex, but not part of hex num
            break
        elif (curr.isnumeric()): # if number
            temp = int(curr)
        elif (curr.isalpha()): # if letter
            curr = curr.lower()
            temp = 10 + (ord(curr) - ord('a')) # get its value
        
        result += (16**mult)*temp
        mult += 1
    
    return result


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        # result = convert(digits, base1, base2)
        print(hexToDigits('A1') == binaryToDigits('1010 0001'))
        # print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

