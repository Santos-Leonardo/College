# Exercise 01.2

arguments = input('Say something: ')
print('Number of characters: ', arguments.__sizeof__() - 25)
print('Reversed: ', arguments[::-1])
