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

balance = 100

def rank(card: tuple) -> int:
    """Returns the rank of a card as an integer."""
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
    """Returns the suit of a card as a string."""
    return card[1]

def draw_cards() -> tuple:
    """Returns a tuple of two lists, each list containing three random cards picked without replacement. One list is the player's hand, the other is the dealer's hand."""
    cards_drawn = random.sample(deck, k = 6)
    hand_1 = sorted(cards_drawn[:3], key = lambda card: rank(card), reverse = True)
    hand_2 = sorted(cards_drawn[3:], key = lambda card: rank(card), reverse = True)
    if hand_1[0][0] == "Ace" and hand_1[1][0] == "3" and hand_1[2][0] == "2":
        hand_1 = [hand_1[1], hand_1[2], hand_1[0]]
    if hand_2[0][0] == "Ace" and hand_2[1][0] == "3" and hand_2[2][0] == "2":
        hand_2 = [hand_2[1], hand_2[2], hand_2[0]]
    return hand_1, hand_2

def hand_ranking(hand: list) -> int:
    """"Checks to see if a hand matches any hand ranking and returns an integer corresponding to the hand ranking."""
    # Straight Flush: returns 5
    if ((rank(hand[0]) - 1 == rank(hand[1]) and rank(hand[1]) - 1 == rank(hand[2])) or (rank(hand[0]) == 3 and rank(hand[1]) == 2 and rank(hand[2]) == 14)) and suit(hand[0]) == suit(hand[1]) and suit(hand[1]) == suit(hand[2]):
        return 5
    # Three-of-a-Kind: returns 4
    elif rank(hand[0]) == rank(hand[1]) and rank(hand[1]) == rank(hand[2]):
        return 4
    # Straight: returns 3
    elif (rank(hand[0]) - 1 == rank(hand[1]) and rank(hand[1]) - 1 == rank(hand[2])) or (rank(hand[0]) == 3 and rank(hand[1]) == 2 and rank(hand[2]) == 14):
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
    """Returns the card of highest rank in a hand."""
    return hand[0]

def ante_wager() -> int:
    """Asks the user how much they'd like to bet on the ante. Keeps asking until a valid number is entered."""
    global balance
    while True:
        try:
            ante = int(input("Ante Wager: "))
            if ante <= 0:
                print("You must bet at least $1.")
            elif ante > balance:
                print("Bet exceeds available balance.")
            else: 
                balance -= ante
                return ante
        except ValueError:
            print("Not a valid number. Try again.")

def play_wager() -> int:
    """Asks the user if they'd like to play or fold. If they choose to play, they must make a play bet, which will be returned. If they choose to fold, return 0."""
    global balance
    while True:
        play_or_fold = input("Enter 'P' if you'd like to keep playing. Enter 'F' if you'd like to fold: ")
        if play_or_fold == 'P' or play_or_fold == 'F':
            break
        else:
            print("Not a valid answer. Try again.")
    if play_or_fold == 'P':
        while True:
            try:
                play = int(input("Play Wager: "))
                if play <= 0:
                    print("You must bet at least $1.")
                elif play > balance:
                    print("Bet exceeds available balance.")
                else: 
                    balance -= play
                    return play
            except ValueError:
                print("Not a valid number. Try again.")
    else:
        return 0

def ante_bonus(hand: list, ante: int):
    """Adds an ante bonus to the player's balance based on what hand ranking they have and returns the ante bonus. If no bonus, return 0."""
    global balance
    # Straight Flush: pays 5:1 on the ante
    if hand_ranking(hand) == 5:
        bonus = ante * 5
        balance += bonus
        return bonus
    # Three-of-a-Kind: pays 4:1 on the ante
    elif hand_ranking(hand) == 4:
        bonus = ante * 4
        balance += bonus
        return bonus
    # Straight: pays 1:1 on the ante
    elif hand_ranking(hand) == 3:
        bonus = ante
        balance += bonus
        return bonus
    else:
        return 0

def compare_hands(player_hand: list, dealer_hand: list) -> str:
    """Compares the player's hand to the dealer's hand and returns the string "Player", "Dealer", or "Push" depending on who won the round (or if it was a tie)."""
    # If the player has a higher hand ranking than the dealer, the player wins.
    if hand_ranking(player_hand) > hand_ranking(dealer_hand):
        return "Player"
    # If the dealer has a higher hand ranking than the dealer, the dealer wins.
    elif hand_ranking(player_hand) < hand_ranking(dealer_hand):
        return "Dealer"
    # If the player and the dealer both have a straight flush, three-of-a-kind, or straight, the hand with the higher high card wins. If they're the same, it's a tie.
    elif hand_ranking(player_hand) == 5 or hand_ranking(player_hand) == 4 or hand_ranking(player_hand) == 3:
        if rank(high_card(player_hand)) > rank(high_card(dealer_hand)):
            return "Player"
        elif rank(high_card(player_hand)) < rank(high_card(dealer_hand)):
            return "Dealer"
        else: 
            return "Push"
    # If the player and the dealer both have a flush or no hand ranking, the hand with the higher high card wins. If they're the same, the hand with the higher second-highest card wins. If those are the same, the hand with the higher third-highest card wins. If those are the same, it's a tie.
    elif hand_ranking(player_hand) == 2 or hand_ranking(player_hand) == 0:
        if rank(high_card(player_hand)) > rank(high_card(dealer_hand)):
            return "Player"
        elif rank(high_card(player_hand)) < rank(high_card(dealer_hand)):
            return "Dealer"
        else:
            if rank(player_hand[1]) > rank(dealer_hand[1]):
                return "Player"
            elif rank(player_hand[1]) < rank(dealer_hand[1]):
                return "Dealer"
            else:
                if rank(player_hand[2]) > rank(dealer_hand[2]):
                    return "Player"
                elif rank(player_hand[2]) < rank(dealer_hand[2]):
                    return "Dealer"
                else:
                    return "Push"
    # If the player and the dealer both have a pair, the pair of higher rank wins. If the pairs have the same rank, the hand with the higher third card wins. If those are the same, it's a tie.
    elif hand_ranking(player_hand) == 1:
        if rank(player_hand[0]) == rank(player_hand[1]) and rank(dealer_hand[0]) == rank(dealer_hand[1]):
            if rank(player_hand[0]) > rank(dealer_hand[0]):
                return "Player"
            elif rank(player_hand[0]) < rank(dealer_hand[0]):
                return "Dealer"
            else:
                if rank(player_hand[2]) > rank(dealer_hand[2]):
                    return "Player"
                elif rank(player_hand[2]) < rank(dealer_hand[2]):
                    return "Dealer"
                else:
                    return "Push"
        elif rank(player_hand[0]) == rank(player_hand[1]) and rank(dealer_hand[1]) == rank(dealer_hand[2]):
            if rank(player_hand[0]) > rank(dealer_hand[1]):
                return "Player"
            elif rank(player_hand[0]) < rank(dealer_hand[1]):
                return "Dealer"
            else:
                if rank(player_hand[2]) > rank(dealer_hand[0]):
                    return "Player"
                elif rank(player_hand[2]) < rank(dealer_hand[0]):
                    return "Dealer"
                else:
                    return "Push"
        elif rank(player_hand[1]) == rank(player_hand[2]) and rank(dealer_hand[0]) == rank(dealer_hand[1]):
            if rank(player_hand[1]) > rank(dealer_hand[0]):
                return "Player"
            elif rank(player_hand[1]) < rank(dealer_hand[0]):
                return "Dealer"
            else:
                if rank(player_hand[0]) > rank(dealer_hand[2]):
                    return "Player"
                elif rank(player_hand[0]) < rank(dealer_hand[2]):
                    return "Dealer"
                else:
                    return "Push"
        elif rank(player_hand[1]) == rank(player_hand[2]) and rank(dealer_hand[1]) == rank(dealer_hand[2]):
            if rank(player_hand[1]) > rank(dealer_hand[1]):
                return "Player"
            elif rank(player_hand[1]) < rank(dealer_hand[1]):
                return "Dealer"
            else:
                if rank(player_hand[0]) > rank(dealer_hand[0]):
                    return "Player"
                elif rank(player_hand[0]) < rank(dealer_hand[0]):
                    return "Dealer"
                else:
                    return "Push"

def is_queen_high(dealer_hand: list) -> bool:
    """Takes the dealer's hand as an input and returns True or False based on whether or not the dealer's hand is at least queen-high. If the dealer's hand is not at least queen-high, the player is paid """
    if rank(high_card(dealer_hand)) >= 12:
        return True
    else:
        return False

def play_again() -> bool:
    """Asks the user if they'd like to play again and returns True or False."""
    while True:
        choice = input("Enter 'Y' if you'd like to play again. Enter 'N' if you'd like to quit: ")
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Not a valid answer. Try again.")

def three_card_poker():
    """Plays the game."""
    global balance
    while True:
        print(f"Balance: {balance}")
        ante = ante_wager()
        player, dealer = draw_cards()
        print(f"Your Hand: {player}")
        play = play_wager()
        if play == 0:
            if play_again():
                print()
                continue
            else:
                break
        else:
            print(f"Dealer's Hand: {dealer}")
            if is_queen_high(dealer) == False:
                print(f"Dealer does not qualify. You win 1 to 1 on the ante and your play wager pushes.")
                balance += (ante * 2 + play)
                print(f"Ante Bonus: {ante_bonus(player, ante)}")
                print(f"Balance: {balance}")
                if play_again():
                    print()
                    continue
                else:
                    break
            else:
                if compare_hands(player, dealer) == "Player":
                    print("Your hand wins. You win 1 to 1 on the ante and on the play wager.")
                    balance += (ante * 2 + play * 2)
                    print(f"Ante Bonus: {ante_bonus(player, ante)}")
                    print(f"Balance: {balance}")
                    if play_again():
                        print()
                        continue
                    else:
                        break
                elif compare_hands(player, dealer) == "Dealer":
                    print("Dealer's hand wins. You lose your wagers.")
                    print(f"Ante Bonus: {ante_bonus(player, ante)}")
                    print(f"Balance: {balance}")
                    if play_again():
                        print()
                        continue
                    else:
                        break
                elif compare_hands(player, dealer) == "Push":
                    print("It's a tie. Your wagers push.")
                    balance += (ante + play)
                    print(f"Ante Bonus: {ante_bonus(player, ante)}")
                    print(f"Balance: {balance}")
                    if play_again():
                        print()
                        continue
                    else:
                        break
    balance = 100

three_card_poker()