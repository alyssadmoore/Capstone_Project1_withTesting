import random
import Card
import Deck

print("Welcome to Go Fish! Here are this version's rules, from https://en.wikipedia.org/wiki/Go_Fish:")
print("1. You may only request a rank in your hand.")
print("2. If you have more than one card with the rank requested, you must hand over all of them.")
print("3. 'Books' are made when you have all four cards of the same rank.")
print("4. The winner is the player with the most books when the deck is empty.\n")
name = input("\nTo start, what is your name?\n")


class Player:

    # Player starts with a hand of 7 cards
    def __init__(self):
        self.player_hand = []
        self.player_sets = []
        a = 0
        b = 7
        while a < b:
            self.player_hand.append(deck.draw_card())
            a += 1

    # Prints all player's cards in-hand
    def show_cards(self):
        if len(self.player_hand) != 0:
            print("Here are your cards:\n----------------------")
            self.player_hand.sort()
            for card in self.player_hand:
                print(card.__str__())

    # Asks the player for a rank to request to the computer. Only ranks in-hand can be requested.
    def get_choice(self):
        while True:
            choice = input("\nWhat rank would you like to request? (Enter Ace, 2, 3, etc.)\n")
            list_a = []
            for x in self.player_hand:
                if x.rank == choice:
                    list_a.append(x.rank)
                    break
            if len(list_a) == 0:
                print("Sorry, you can only request a rank in your hand. Please try again.")
            else:
                break
        return choice

    # Always show the player their cards before requesting their choice
    def take_turn(self):

        player.show_cards()

        # As long as the player has a hand, they must make a guess.
        # Even though guessing is redundant when comp's hand is empty, this is taken care of by
        # returning an empty list of possible matches, and then the player draws a card anyway
        if len(self.player_hand) != 0:

            choice = self.get_choice()
            hand_over = []

            # A list of matching cards are created because all matches must be handed over
            for i in computer.comp_hand:
                if i.rank == choice:
                    hand_over.append(i)

            # A message is displayed for each card that is handed over
            for j in hand_over:
                print("Computer gives you " + Card.Card.__str__(j) + ".")
                self.player_hand.append(j)
                computer.comp_hand.remove(j)

            # If no matches are found, "Go fish" and draw from the deck
            if len(hand_over) == 0:
                print("Sorry, go fish!")
                card = deck.draw_card()
                self.player_hand.append(card)
                print("You fished a(n) " + Card.Card.__str__(card) + ".\n")

            # Always check for a match in-hand after turn
            if check_match_in_hand(self.player_hand):
                self.player_sets.append("1")
                print("You played a book.\n")
                self.show_cards()
                print("\nCurrent scores:\n" + name + ": " + str(len(self.player_sets)))
                print("Computer: " + str(len(computer.comp_sets)) + "\n")

        # If the player doesn't have a hand, they can't make a guess, so they must draw a card if the deck remains
        if (len(self.player_hand) == 0) and (len(deck.deck) != 0):
            print("You have nothing in hand! Go fishing.")
            card = deck.draw_card()
            self.player_hand.append(card)
            print("You fished a(n) " + Card.Card.__str__(card) + ".\n")

        # If the player doesn't have a hand and the deck is gone, they have nothing they can do. No action taken


class Computer:

    # Computer starts with a hand of 7 cards, empty list to hold points (comp_sets)
    def __init__(self):
        self.comp_hand = []
        self.comp_sets = []
        a = 0
        b = 7
        while a < b:
            self.comp_hand.append(deck.draw_card())
            a += 1

    # Computer's hand order is randomized each turn, first choice is to guess the last card in hand's rank
    def comp_turn(self):
        random.shuffle(self.comp_hand)
        comp_guess = 1

        # If either computer's or player's hand is empty AND the deck remains, comp must draw from the deck
        # (comp has nothing in hand to guess from, or player has nothing to give to the computer)
        if (len(self.comp_hand) == 0 or len(player.player_hand) == 0) and (len(deck.deck) != 0):
            print("Nothing in comp hand or nothing in player hand; comp must go fishing.")
            self.comp_hand.append(deck.draw_card())

        # If either computer's or player's hand is empty AND the deck is empty, skip to checking match in-hand
        # (comp has nothing in hand to guess from, or player has nothing to give, and the deck is empty)
        if (len(self.comp_hand) == 0 or len(player.player_hand) == 0) and (len(deck.deck) == 0):
            if check_match_in_hand(self.comp_hand):
                self.comp_sets.append("1")
                print("Computer lays down a book.")
                print("\nCurrent scores:\n" + name + ": " + str(len(player.player_sets)))
                print("Computer: " + str(len(self.comp_sets)) + "\n")

        # First guess is only reached if it is determined possible to request a card
        else:
            for x in self.comp_hand:
                comp_guess = x.rank

        # If comp's guess is a legitimate guess, it will have changed from 1 to something else
        # Everything else in this block is very similar to Player's take_turn block
        if comp_guess != 1:

            print("Computer's turn. Thinking...\nComputer requests a(n) " + str(comp_guess) + ".")
            hand_over = []

            for i in player.player_hand:
                if i.rank == str(comp_guess):
                    hand_over.append(i)

            for j in hand_over:
                print("You give the computer a(n) " + Card.Card.__str__(j) + ".")
                self.comp_hand.append(j)
                player.player_hand.remove(j)

            if len(hand_over) == 0:
                print("Computer goes fishing.\n")
                self.comp_hand.append(deck.draw_card())

            if check_match_in_hand(self.comp_hand):
                self.comp_sets.append("1")
                print("Computer lays down a book.")
                print("\nCurrent scores:\n" + name + ": " + str(len(player.player_sets)))
                print("Computer: " + str(len(self.comp_sets)) + "\n")


# Checks if there is a book in-hand (comp or player)
def check_match_in_hand(hand):
    for i in hand:
        rank = i.rank
        suit = i.suit
        matches = []
        for j in hand:
            if j.rank == rank and j.suit != suit:
                matches.append(j)
        if len(matches) == 3:
            hand.remove(i)
            hand.remove(matches[0])
            hand.remove(matches[1])
            hand.remove(matches[2])
            return True


# Checks who won when the deck is empty. Because there are 13 sets in a deck, there is no scenario with a tie.
def check_deck_empty():
    if len(deck.deck) == 0:
        if len(computer.comp_sets) > len(player.player_sets):
            print("Deck empty; Computer wins!\n")
            check_high_scores(len(player.player_sets))
        if len(computer.comp_sets) < len(player.player_sets):
            print("Deck empty; " + name + " wins!\n")
            check_high_scores(len(player.player_sets))
        return True


def check_high_scores(score):

    names_list = []
    line_to_delete = ""

    # This block reads all lines in high score file, separates scores from names and adds both to separate lists,
    # then checks if score this game is a new high score for the player. If so, set the line to rewrite as a variable
    try:
        scores1 = open("high_scores.txt", "r")
        lines = scores1.readlines()
        for line in lines:
            name_and_score = line.split(": ")
            # Only continue if there is at least one high score entry, compare old score to new score
            if len(name_and_score) > 1:
                just_score = name_and_score[1].split("\n")
                just_name = name_and_score[0]
                names_list.append(just_name)
                if (int(score) > int(just_score[0])) and (name == just_name):
                    print("You got a new high score!")
                    line_to_delete = name + ": " + str(just_score[0]) + "\n"
        scores1.close()

        # This block takes all previous scores (from the above block), except for the score to be rewritten, and
        # overwrites the high scores file with previous scores plus the updated score (or new score if new player)
        scores2 = open("high_scores.txt", "w")
        for line in lines:
            if line != line_to_delete:
                scores2.write(line)
        scores2.write(name + ": " + str(score) + "\n")
        scores2.close()

    except Exception:
        print("Sorry, there was an error reading the high scores file.")

    # Always present the full list of high scores
    print("High Scores:\n------------------------")
    try:
        all_scores = open("high_scores.txt", "r")
        scores = all_scores.read()
        print(scores)
        all_scores.close()
    except Exception:
        print("Sorry, there was an error reading from the high scores file.")


# Creating instances of Deck, Player and Computer objects
deck = Deck.Deck()
player = Player()
computer = Computer()

while True:
    # Player always goes first, checks if game is done after each turn. Repeat with computer's turn until game over.
    player.take_turn()
    if check_deck_empty():
        break

    computer.comp_turn()
    if check_deck_empty():
        break
