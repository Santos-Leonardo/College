# Exercise 01.3
# Author: Leonardo Ferreira Santos


def quadratic(a, b, c):
    delta = (b ** 2 - 4 * a * c)
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    solution = 0
    if type(x1) != complex:
        solution = solution + 1

    if type(x2) != complex:
        solution = solution + 1

    print('\nSolutions: ', solution)

    if solution > 0:
        print('\nX1 = ', x1)
        print('X2 = ', x2)


a = int(input('Enter the value of A: '))
b = int(input('Enter the value of B: '))
c = int(input('Enter the value of C: '))

quadratic(a, b, c)
