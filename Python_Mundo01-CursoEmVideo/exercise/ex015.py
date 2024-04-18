# Create a program that reads the number of km traveled by the rental car and the number of rental days
# and displays the price to be paid, knowing that each day costs $60 and each km costs $0.15:

days = int(input('Enter how many days you rented the car: '))
kms = int(input('Enter how many km you drove the car: '))

priceDays = days * 60
priceKms = kms * 0.15
priceTotal = priceDays + priceKms

print(f'The total to pay for the car rental is {priceTotal}!')
