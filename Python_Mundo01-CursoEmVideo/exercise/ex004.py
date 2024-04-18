# Create a program that reads what was typed and returns its type and other information about it:

userInput = input('Enter something: ')

print(f'Data type: {type(userInput)}')
print(f'It\'s alphanumeric: {userInput.isalnum()}')
print(f'It\'s alphabetical: {userInput.isalpha()}')
print(f'It\'s numeric: {userInput.isnumeric()}')
print(f'It\'s in upper case: {userInput.isupper()}')
print(f'It\'s in lower case: {userInput.islower()}')
print(f'It\'s capitalized: {userInput.istitle()}')
