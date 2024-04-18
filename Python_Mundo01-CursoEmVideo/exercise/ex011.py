# Create a program that reads the width and height of a wall and calculates the area
# and amount of paint needed to paint it, knowing that 1 liter of paint paints 2 square meters:

width = float(input('How wide is the wall?'))
height = float(input('How tall is the wall?'))

area = width * height
paintLiter = area / 2

print(f'A {area} square meter wall needs {paintLiter} liters of paint!')
