import random
#random module gives us the shuffle function to randomize the card order of the deck list


class Deal:
    deck = []
    current_card = 0
    next_card = 0

    def __init__(self):
        print()

    def get_card(self):
        # gets the current card value
        return self.current_card

    def get_next_card(self):
        # gets the next card value
        return self.next_card

    def deal_card(self):
        # checks to see if there enough cards in the deck to play another round, then selects the next 2 cards
        if len(self.deck) < 2:
            self.shuffle_deck()
            return None
        else:
            self.current_card = self.deck[-1]
            self.deck.pop()
            self.next_card = self.deck[-1]
            self.deck.pop()

            return self.get_card()

    def shuffle_deck(self):
        # This function is to shuffle the list of numbers 1-13. While playing the game each next_card will be pulled from the
        # list of numbers in sequential order. When the player quits or runs out of cards the dealer will re-shuffle by
        # running this function
        for i in range(13):
            self.deck.append(i + 1)
        random.shuffle(self.deck)

        if self.deal_card() == None:
            return None
        else:
            return self.deal_card()
