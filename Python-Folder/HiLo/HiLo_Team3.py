from hilo import HiLo
import random
#random module gives us the shuffle function to randomize the card order of the deck list
import sys
#sys module gives us the exit function so the player can choose to finish using the program

def main():
    hilo_game = HiLo()
    hilo_game.start_game()


def shuffle_deck ():
    # This function is to shuffle the list of numbers 1-13. While playing the game each next_card will be pulled from the
    # list of numbers in sequential order. When the player quits or runs out of cards the dealer will re-shuffle by 
    # running this function
    global deck
    deck = []
    for i in range(13):
        deck.append(i+1) 
    random.shuffle(deck)
    print(deck)
    select_cards()

def select_cards():
    #checks to see if there enough cards in the deck to play another round, then selects the next 2 cards 
    global deck
    if len(deck) < 2:
        shuffle_deck()
    else:
        current_card = deck[-1]
        deck.pop()
        next_card = deck[-1]
        deck.pop()
        player_interface(current_card, next_card)

def player_interface(current_card,next_card):
    #runs the player input section of the program, (where the player actually plays the game)
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
    score_changer(player_choice, current_card, next_card)
    if player_score == 0:
        print()
        print("Oops, you are out of points. Game over.")
        check_high_score()
    while True:
        play_again = input("Keep playing? [y/n] ")
        play_again = play_again.lower()
        print()
        if play_again == "y" or play_again == "yes":
            select_cards()
        elif play_again == "n" or play_again == "no":
            print("Round complete.")
            check_high_score()
        else:
            print("Invalid Input.")
            print()

def score_changer(player_choice, current_card, next_card):
    #changes the player score depending on if the player guessed right
    global player_score
    win = "Congrats, you guessed right and won 100 points!"
    lose = "Sorry, you guessed wrong and lost 75 points."
    if player_choice == "h" or player_choice == "H":
        if current_card < next_card:
            print(win)
            player_score += 100
        else:
            print(lose)
            player_score -= 75
    elif player_choice == "l" or player_choice == "L":
        if current_card > next_card:
            print(win)
            player_score += 100
        else:
            print(lose)
            player_score -= 75
    if player_score <= 0:
        player_score = 0
    print(f"Your score is: {player_score}")



def check_high_score():
    #Determines whether last round had the new high score
    global high_score
    print()
    print(f"You finished this round of HiLo with {player_score} points.")
    print()
    if high_score < player_score:
        high_score = player_score
        print("Congratulations on getting the new High Score!")
        print()
    print(f"The current High Score is {high_score} points.")
    print()
    restart()


def restart():
    #gives the player to ability to start a new round of HiLo or finish playing
    while True:
        restart = input("Would you like to play another round? (y/n): ")
        restart = restart.lower()
        print()
        if restart == "y" or restart == "yes":
            main()
        elif restart == "n" or restart == "no":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid Input.")
            print()



if __name__ == "__main__":
    main()