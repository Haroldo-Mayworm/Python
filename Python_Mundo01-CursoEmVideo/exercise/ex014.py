# Create a program that reads the temperature in Celsius and displays the conversion in Fahrenheit

tCelsius = float(input('Enter tha temperature in Celsius: '))

tFahrenheit = (tCelsius * 9/5) + 32

print(f'{tCelsius} degrees Celsius are equivalent to {tFahrenheit:.2f} degrees Fahrenheit')
