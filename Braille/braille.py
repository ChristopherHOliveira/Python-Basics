def solution(s):
    r = ''
    for c in s:
        if c.lower() == ' ':
            r += '000000'
        if c.isupper():
            r += '000001'
        if c.lower() == 'a':
            r += '100000'
        if c.lower() == 'b':
            r += '110000'
        if c.lower() == 'c':
            r += '100100'
        if c.lower() == 'd':
            r += '100110'
        if c.lower() == 'e':
            r += '100010'
        if c.lower() == 'f':
            r += '110100'
        if c.lower() == 'g':
            r += '110110'
        if c.lower() == 'h':
            r += '110010'
        if c.lower() == 'i':
            r += '010100'
        if c.lower() == 'j':
            r += '010110'
        if c.lower() == 'k':
            r += '101000'
        if c.lower() == 'l':
            r += '111000'
        if c.lower() == 'm':
            r += '101100'
        if c.lower() == 'n':
            r += '101110'
        if c.lower() == 'o':
            r += '101010'
        if c.lower() == 'p':
            r += '111100'
        if c.lower() == 'q':
            r += '111110'
        if c.lower() == 'r':
            r += '111010'
        if c.lower() == 's':
            r += '011100'
        if c.lower() == 't':
            r += '011110'
        if c.lower() == 'u':
            r += '101001'
        if c.lower() == 'v':
            r += '111001'
        if c.lower() == 'w':
            r += '010111'
        if c.lower() == 'x':
            r += '101101'
        if c.lower() == 'y':
            r += '101111'
        if c.lower() == 'z':
            r += '101011'

    return r


# Testing example:

test1_answer = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'

test1 = solution('The quick brown fox jumps over the lazy dog')

if test1_answer == test1:
    print('Test 1 passed.')
