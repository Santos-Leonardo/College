# Exercise 01

print('Those are the operation allowed:')
print()

print('Sum = +')
print('Subtraction = -')
print('Multiplication = *')
print('Division = /')
print()

operation = input('Insert the operation: ')
number1 = int(input('Insert the first number: '))
number2 = int(input('Insert the second number: '))

if operation == '+':
    print(number1 + number2)

elif operation == '-':
    print(number1 - number2)

elif operation == '*':
    print(number1 * number2)

elif operation == '/':
    print(number1 / number2)

else:
    print('An error has happened.')
