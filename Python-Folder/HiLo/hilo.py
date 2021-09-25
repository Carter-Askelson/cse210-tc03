from deal import Deal

import sys
#sys module gives us the exit function so the player can choose to finish using the program





class HiLo:
    player_score = 300
    high_score = 0
    deal = Deal()

    def start_game(self):
        self.game_rules()
        shuffled_deck = self.deal.shuffle_deck()

        if shuffled_deck is not None:
            self.player_interface(self.deal.current_card, self.deal.next_card)

    def game_rules(self):
        print("Rules to HighLo: ")
        print("Hilo is played according to the following rules. \n \
        •Individual cards are represented as a number from 1 to 13. \n\
        •The player starts the game with 300 points.\n\
        •The dealer displays the current card.\n\
        •The player guesses if the next one will be higher or lower.\n\
        •The dealer shows the next card.\n\
        •The player earns 100 points if they guessed correctly.\n\
        •The player loses 75 points if they guessed incorrectly.\n\
        •If a player reaches 0 points the game is over. Otherwise, the player decides whether or not to play again.\n\
        •If a player decides not to play again the game is over.")
        print()
        print("Starting new game of HiLo")
        print()
        self.deal.shuffle_deck()

    def player_interface(self, current_card, next_card):
        # runs the player input section of the program, (where the player actually plays the game)
        print(f"The 1st card is: {current_card}")
        while True:
            player_choice = input("Higher or lower? [h/l] ")
            approved_inputs = ("h", "H", "l", "L")
            if player_choice in approved_inputs:
                print()
                break
            else:
                print("Invalid Input.")
                print()
        print(f"The 2nd card is: {next_card}")
        self.score_changer(player_choice, current_card, next_card)
        if self.player_score == 0:
            print()
            print("Oops, you are out of points. Game over.")
            self.check_high_score()
        while True:
            play_again = input("Keep playing? [y/n] ")
            play_again = play_again.lower()
            print()
            if play_again == "y" or play_again == "yes":
                selected_card = self.deal.deal_card()
                if selected_card is not None:
                    self.player_interface(self.deal.current_card, self.deal.next_card)
            elif play_again == "n" or play_again == "no":
                print("Round complete.\n")
                self.check_high_score()
                self.restart()
            else:
                print("Invalid Input.")
                print()

    def restart(self):
        # gives the player to ability to start a new round of HiLo or finish playing
        while True:
            restart = input("Would you like to play another round? (y/n): ")
            restart = restart.lower()
            print()
            if restart == "y" or restart == "yes":
                self.start_game()
            elif restart == "n" or restart == "no":
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Invalid Input.")
                print()

    def check_high_score(self):
        # Determines whether last round had the new high score
        print()
        print(f"You finished this round of HiLo with {self.player_score} points.")
        print()
        if self.high_score < self.player_score:
            self.high_score = self.player_score
            print("Congratulations on getting the new High Score!")
            print()
        print(f"The current High Score is {self.high_score} points.")
        print()

    def score_changer(self, player_choice, current_card, next_card):
        # changes the player score depending on if the player guessed right
        win = "Congrats, you guessed right and won 100 points!"
        lose = "Sorry, you guessed wrong and lost 75 points."
        if player_choice == "h" or player_choice == "H":
            if current_card < next_card:
                print(win)
                self.player_score += 100
            else:
                print(lose)
                self.player_score -= 75
        elif player_choice == "l" or player_choice == "L":
            if current_card > next_card:
                print(win)
                self.player_score += 100
            else:
                print(lose)
                self.player_score -= 75
        if self.player_score <= 0:
            self.player_score = 0
        print(f"Your score is: {self.player_score}")
