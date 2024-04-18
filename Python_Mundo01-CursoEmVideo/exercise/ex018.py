# Create a program that reads an angle and displays its sine, cosine and tangent of that angle.

import math

angleInput = int(input('Enter the angle: '))

angleRadians = math.radians(angleInput)

sine = math.sin(angleRadians)
cosine = math.cos(angleRadians)
tangent = math.tan(angleRadians)

print(f'Sine: {sine:.3f}')
print(f'Cosine: {cosine:.3f}')
print(f'Tangent: {tangent:.3f}')
