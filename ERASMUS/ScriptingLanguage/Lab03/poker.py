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


def is_rank_sequence(hand):

    # It has to be implemented
    return true


def hand_rank(hand):

    hand_rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    hand_color_list = ['c', 'd', 'h', 's']

    hand_rank_histogram = histogram(hand_rank_list)
    # Histogram of suits, if 5 in hand_color_histogram.values() == True
    # than all of the cards are in the same suit
    hand_color_histogram = histogram(hand_color_list)
    # We want to find if the hand contains five cards of sequential rank
    # TODO: implement function is_rank_sequence(hand) which returns true if so
    is_hand_rank_sequence = is_rank_sequence(hand) 

    hand_strength = 0

    # royal flush: 5 cards of sequential rank, all of the same suit, Ace is the highest
    if (5 in hand_color_histogram.values()) and ('A' in hand_rank_list) and is_hand_rank_sequence:
        hand_strength = 10

    # straight flush: 5 cards of sequential rank, all of the same suit
    elif (5 in hand_color_histogram.values()) and is_hand_rank_sequence:
        hand_strength = 9

    # four of a kind: four cards of the same rank and one card of another rank
    elif 4 in hand_rank_histogram.keys():
        hand_strength = 8

    # full house: three cards of one rank and two cards of another rank
    elif (3 in hand_rank_histogram.keys()) and (2 in hand_rank_histogram.keys()):
        hand_strength = 7

    # flush: five cards all of the same suit, not all of sequential rank
    elif 5 in hand_color_histogram.values():
        hand_strength = 6

    # straight: five cards of sequential rank, not all of the same suit
    elif (5 in hand_rank_histogram.keys()) and is_hand_rank_sequence:
        hand_strength = 5

    # three of a kind: three cards of the same rank and two cards of two other ranks
    elif (3 in hand_rank_histogram.keys()) and (2 in hand_rank_histogram.keys()):
        hand_strength = 4

    # two pair: two cards of the same rank, two cards of another rank and one card of a third rank
    elif (3 in hand_rank_histogram.keys()) and (2 in hand_rank_histogram.keys()):
        hand_strength = 3

    # one pair: two cards of the same rank and three cards of three other ranks
    elif 2 in hand_rank_histogram.keys():
        hand_strength = 2
    # high card: five cards not all of sequential rank or of the same suit, and none of which are of the same rank
    else:
        hand_strength = 1

    return hand_strength
