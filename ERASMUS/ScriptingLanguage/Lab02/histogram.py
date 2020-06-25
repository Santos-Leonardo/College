# Exercise 02.1: Histogram
# Author: Leonardo Ferreira Santos


def histogram(phase):

    dictionary = {}

    i = 0
    while i < len(phase):

        if phase[i] in dictionary:
            dictionary[phase[i]] = dictionary.get(phase[i]) + 1

        else:
            dictionary[phase[i]] = 1

        i = i + 1

    return dictionary


phase = input('Say something: ')
print(histogram(phase))
