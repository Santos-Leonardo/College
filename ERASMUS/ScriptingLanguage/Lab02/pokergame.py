# Exercise 02.2: Poker Game
# Author: Leonardo Ferreira Santos

import random


# This function creates the deck
def deck():

    rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    color_list = ['c', 'd', 'h', 's']

    deck = []

    i = 0
    j = 0

    while i < len(rank_list):

        while j < len(color_list):
            card = (rank_list[i], color_list[j])
            deck.append(card)
            j += 1

        i += 1
        j = 0

    return deck


# This function will return a shuffled deck
def shuffle_deck(deck):

    random_deck = random.sample(deck, 5)
    return random_deck


def deal(deck, n):

    deck_number = 1
    decks = []

    while deck_number <= n:

        new_deck = shuffle_deck(deck)
        decks.append(new_deck)

        deck_number += 1

    return decks


print('---Pocker Cards---\n')

n = int(input('Number os players: '))

print(deal(deck(), n))