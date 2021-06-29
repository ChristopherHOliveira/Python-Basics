This program contains a function which encodes any string value into another string containing its Braille version.
The initial string must be passed as a parameter of the function.
Braille codes for each string character are represented with 6 dots (or absense of dots) which can be interpreted by the touch.

e.g. character 'o' in braille =

1 0
0 1
1 0

Here the '0' represents the absense of dot and '1' a dot. It is read starting from the left column, top to bottom and so on.
In this program, each character will be represented as a linear Braille string of the character, therefore the 'o' example should return '101010'.
