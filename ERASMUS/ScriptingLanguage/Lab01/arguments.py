# Exercise 01.2
# Author: Leonardo Ferreira Santos

arguments = input('Say something: ')
print('Number of characters: ', arguments.__sizeof__() - 25) # "-25" is necessary because this function always implements "25".
print('Reversed: ', arguments[::-1])
