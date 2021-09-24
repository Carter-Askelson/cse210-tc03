import random 
print("Rules to HighLo: ")
print("Hilo is played according to the following rules. \n \
•Individual cards are represented as a number from 1 to 13. \n\
 •The player starts the game with 300 points.\n\
 •The dealer displays the current card.\n\
 •The player guesses if the next one will be higher or lower.\n\
 •The dealer shows the next card.\n\
 •The player earns 100 points if they guessed correctly.\n\
 •The player loses 75 points if they guessed incorrectly.\n\
 •If a player reaches 0 points the game is over. Otherwise, the player decideswhether or not to play again.\n\
 •If a player decides not to play again the game is over.")



player_score = 300

def shuffle_deck (numbers):
    numbers = []
    for i in range(13):
        numbers.append(i+1) 
    # This function is to shuffle the list of numbers 1-13. While playing the game each next_card will be pulled from the
    # list of numbers in sequential order. When the player quits or runs out of cards the dealer will re-shuffle by 
    # running this function
    random.shuffle(numbers)
    return numbers

def interface (current_card,next_card,player_score):
    print(f"The card is: {current_card}")
    player_choice = input("Higher or lower? [h/l] ")
    print(f"Next card was: {next_card}")
    print(f"Your score is: {player_score}")
    play_again = input("Keep playing? [y/n] ")


# def player_score ():

