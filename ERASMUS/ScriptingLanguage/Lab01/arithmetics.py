# Exercise 01.1
# Author: Leonardo Ferreira Santos

print('Those are the operation allowed:\n')

print('Sum = +')
print('Subtraction = -')
print('Multiplication = *')
print('Division = /')

operation = input('\nInsert the operation: ')
number1 = int(input('Insert the first number: '))
number2 = int(input('Insert the second number: '))

if operation == '+':
    print('Result: ', number1 + number2)

elif operation == '-':
    print('Result: ', number1 - number2)

elif operation == '*':
    print('Result: ', number1 * number2)

elif operation == '/':
    print('Result: ', number1 / number2)

else:
    print('\nInvalid operation')
