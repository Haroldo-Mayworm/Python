# Create a program that reads a value and displays how many dollars can be purchased:

moneyReal = float(input('Enter how much money you have: '))

exchangeRate = 3.27
moneyDollar = moneyReal / exchangeRate

print(f'With R${moneyReal} you can buy ${moneyDollar:.2f}')
