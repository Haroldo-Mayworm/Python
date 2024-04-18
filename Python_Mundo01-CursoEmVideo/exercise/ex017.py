# Create a program that reads the length of the opposite and adjacent sides of a right triangle
# and calculates the length of the hypotenuse:

import math

opposite = int(input('Enter the opposite side: '))
adjacent = int(input('Enter the adjacent side: '))

hypotenuse = math.sqrt(opposite ** 2 + adjacent ** 2)

print(hypotenuse)
