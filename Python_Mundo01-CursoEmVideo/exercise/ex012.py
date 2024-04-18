# Create a program that reads the price of a product and displays a new price with a 5% discount:

oldPrice = float(input('Enter the product price: '))

discount = 0.05
newPrice = oldPrice - (oldPrice * discount)

print(f'The product will cost ${newPrice}')
