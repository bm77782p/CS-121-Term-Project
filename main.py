import random

deck = [
    ("Ace", "Spades"),
    ("2", "Spades"),
    ("3", "Spades"),
    ("4", "Spades"),
    ("5", "Spades"),
    ("6", "Spades"),
    ("7", "Spades"),
    ("8", "Spades"),
    ("9", "Spades"),
    ("10", "Spades"),
    ("Jack", "Spades"),
    ("Queen", "Spades"),
    ("King", "Spades"),

    ("Ace", "Clubs"),
    ("2", "Clubs"),
    ("3", "Clubs"),
    ("4", "Clubs"),
    ("5", "Clubs"),
    ("6", "Clubs"),
    ("7", "Clubs"),
    ("8", "Clubs"),
    ("9", "Clubs"),
    ("10", "Clubs"),
    ("Jack", "Clubs"),
    ("Queen", "Clubs"),
    ("King", "Clubs"),

    ("Ace", "Diamonds"),
    ("2", "Diamonds"),
    ("3", "Diamonds"),
    ("4", "Diamonds"),
    ("5", "Diamonds"),
    ("6", "Diamonds"),
    ("7", "Diamonds"),
    ("8", "Diamonds"),
    ("9", "Diamonds"),
    ("10", "Diamonds"),
    ("Jack", "Diamonds"),
    ("Queen", "Diamonds"),
    ("King", "Diamonds"),

    ("Ace", "Hearts"),
    ("2", "Hearts"),
    ("3", "Hearts"),
    ("4", "Hearts"),
    ("5", "Hearts"),
    ("6", "Hearts"),
    ("7", "Hearts"),
    ("8", "Hearts"),
    ("9", "Hearts"),
    ("10", "Hearts"),
    ("Jack", "Hearts"),
    ("Queen", "Hearts"),
    ("King", "Hearts")
]

def rank(card: tuple) -> int:
    # Returns the rank of a card as an integer.
    if card[0] == "2":
        return 2
    elif card[0] == "3":
        return 3
    elif card[0] == "4":
        return 4
    elif card[0] == "5":
        return 5
    elif card[0] == "6":
        return 6
    elif card[0] == "7":
        return 7
    elif card[0] == "8":
        return 8
    elif card[0] == "9":
        return 9
    elif card[0] == "10":
        return 10
    elif card[0] == "Jack":
        return 11
    elif card[0] == "Queen":
        return 12
    elif card[0] == "King":
        return 13
    elif card[0] == "Ace":
        return 14

def suit(card: tuple) -> str:
    # Returns the suit of a card an a string.
    return card[1]

def draw_cards() -> tuple:
    # Returns a tuple of two lists, each list containing three random cards picked without replacement. 
    # One list is the player's hand, the other is the dealer's hand.
    cards_drawn = random.sample(deck, k = 6)
    hand_1 = sorted(cards_drawn[:3], key = lambda card: rank(card), reverse = True)
    hand_2 = sorted(cards_drawn[3:], key = lambda card: rank(card), reverse = True)
    if hand_1[0][0] == "Ace" and hand_1[1][0] == "3" and hand_1[2][0] == "2":
        hand_1 = [hand_1[1], hand_1[2], hand_1[0]]
    if hand_2[0][0] == "Ace" and hand_2[1][0] == "3" and hand_2[2][0] == "2":
        hand_2 = [hand_2[1], hand_2[2], hand_2[0]]
    return hand_1, hand_2

def hand_ranking(hand: list) -> int:
    # Checks to see if a hand matches any hand ranking and returns an integer corresponding to the hand ranking.
    # Straight Flush: returns 5
    if rank(hand[0]) - 1 == rank(hand[1]) and rank(hand[1]) - 1 == rank(hand[2]) and suit(hand[0]) == suit(hand[1]) and suit(hand[1]) == suit(hand[2]):
        return 5
    # Three-of-a-Kind: returns 4
    elif rank(hand[0]) == rank(hand[1]) and rank(hand[1]) == rank(hand[2]):
        return 4
    # Straight: returns 3
    elif rank(hand[0]) - 1 == rank(hand[1]) and rank(hand[1]) - 1 == rank(hand[2]):
        return 3
    # Flush: returns 2
    elif suit(hand[0]) == suit(hand[1]) and suit(hand[1]) == suit(hand[2]):
        return 2
    # Pair: returns 1
    elif rank(hand[0]) == rank(hand[1]) or rank(hand[1]) == rank(hand[2]):
        return 1
    # None: returns 0
    else:
        return 0

def high_card(hand: list) -> tuple:
    # Returns the card of highest rank in a hand.
    return hand[0]