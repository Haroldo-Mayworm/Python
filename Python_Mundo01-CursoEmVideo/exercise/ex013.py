# Create a program that reads an employee's salary and displays the salary with a 15% increase

oldSalary = float(input('Enter the salary: '))

increase = 0.15
newSalary = oldSalary + (oldSalary * increase)

print(f'The salary will be ${newSalary}')
