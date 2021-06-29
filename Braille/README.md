This program contains a function which encodes any string value into another string containing its Braille version.

The initial string must be passed as a parameter of the function.

Braille codes for each string character are represented with 6 dots (or absense of dots) in 2 columns, which can be interpreted by the touch. It is read starting from the left column, top to bottom and so on.

In this program, each character of the string passed as argument will be represented as a linear Braille string of the character. '0' represents the absense of dot and '1' a dot. Therefore 'o', for example, should return '101010'.
