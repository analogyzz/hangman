import random
# assuming words.py contains a list or set named 'words'
from words import words
import string # needed for string.ascii_uppercase

# function to get a valid word from the list/set
def get_valid_word(words):
    """
    chooses a random word from the input list/set of words,
    ensuring it does not contain hyphens or spaces.

    args:
        words: a list or set of strings (potential words for the game).

    returns:
        a string: a randomly chosen word without hyphens or spaces, in uppercase.
    """
    # convert the input collection (set or list) to a list
    # to ensure random.choice works reliably with indexing internally
    word_list = list(words)

    # randomly chooses a word from the list
    word = random.choice(word_list)
    # keep choosing until we get a word without hyphens or spaces
    while '-' in word or ' ' in word:
        word = random.choice(word_list) # choose from the list again if the word is invalid

    # return the chosen word in uppercase
    return word.upper()

# main hangman game function for a single round
def hangman():
    """
    runs a single round of the hangman game.
    the user guesses letters to find a hidden word within a limited number of lives.
    """
    # get the secret word for this round
    word = get_valid_word(words)

    # create a set of the original unique letters in the word (used for checking guesses)
    word_set = set(word)

    # create a set of unique letters that still need to be guessed
    # initially, this is the same as word_set, letters are removed as they are guessed correctly
    word_letters = set(word)

    # create a set of all uppercase letters in the alphabet
    alphabet = set(string.ascii_uppercase)

    # create an empty set to store all letters the user has guessed so far (correct or incorrect)
    used_letters = set()

    # --- add lives ---
    lives = 6 # initialize the number of lives
    # ---------------

    # --- the main game loop ---
    # the loop continues as long as there are letters left to guess and lives > 0
    while len(word_letters) > 0 and lives > 0: # change the loop condition here
        # --- displaying current game status ---
        # display the current number of lives
        print(f'\nYou have {lives} lives left.')

        # calculate and display correct guesses (letters in word_set AND used_letters)
        correct_guesses = word_set & used_letters # set intersection
        print('Correct guesses: ', ' '.join(correct_guesses))

        # calculate and display incorrect guesses (letters in used_letters but not in word_set)
        incorrect_guesses = used_letters - word_set # set difference
        print('Incorrect guesses: ', ' '.join(incorrect_guesses))

        # display the current state of the secret word (revealed letters and hyphens)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ',' '.join(word_list))
        # -----------------------------------


        # --- getting and processing user input ---
        user_letter = input('please guess a letter:').upper()

        # check if the guessed letter is a valid uppercase letter AND has not been used before
        if user_letter in alphabet - used_letters:
             # if the guess is valid and not used
             used_letters.add(user_letter) # add the letter to the set of all used letters

             # check if the valid, unused letter is in the secret word
             if user_letter in word_letters:
                 # if the guess is correct (it was in the word)
                 word_letters.remove(user_letter) # remove the letter from the set of letters left to guess
                 print(f'\ngood guess! "{user_letter}" was in the word.😁') # positive feedback

             else:
                 # if the guess is incorrect (valid letter, but not in the word)
                 lives -= 1 # decrement life here! (use the -= operator or lives = lives - 1)
                 print(f'\nsorry, "{user_letter}" is not in the word.😰') # negative feedback


        elif user_letter in used_letters:
            # if the guess has already been used
            print('\nyou have already used that character. please try again.') # add \n for a new line
            # no life lost for guessing an already used letter

        else:
            # if the input is not a valid uppercase letter from the alphabet
            print('\ninvalid character. please try again.') # add \n for a new line
            # no life lost for invalid input
        # -------------------------------------------


    # --- code executed when the main loop condition is no longer true ---
    # the loop stops when len(word_letters) == 0 (win) OR when lives == 0 (lose)
    # check which condition made the loop stop to determine win or loss
    if lives == 0: # check if lost because lives ran out
        print(f'\nyou died, sorry, the word was "{word}"!!💀') # loss message
    else: # if not lost because lives ran out, then user won (because word_letters is 0)
        print(f'\nyay! you guessed the word "{word}"!!🎉') # win message


# --- main function to run multiple rounds of the hangman game ---
def main_hangman_game():
    """
    runs multiple rounds of the hangman game until the user chooses to stop.
    """
    # initialize the variable to control playing again
    play_again = 'y'

    # loop to run the game multiple times as long as play_again is 'y'
    while play_again == 'y':
        # call the hangman() function to play a single round
        hangman()

        # after a round is finished, ask the user if they want to play again
        # use an inner loop to validate the 'play again' input
        while True:
            play_again_input = input("\ndo you want to play again? (y/n): ").lower() # get yes/no input and convert to lowercase
            # validate if the input is 'y' or 'n'
            if play_again_input in ['y', 'n']:
                # if valid, update the control variable for the main loop
                play_again = play_again_input
                # exit the 'play again' input validation loop
                break
            else:
                # error message if 'play again' input is invalid
                print("invalid input. please enter 'y' or 'n'.")

    # message displayed when the main loop ends (user entered 'n')
    print("\nthanks for playing hangman!")

# --- starting the entire program ---
# this is the only line outside of function definitions that runs initially.
print("welcome to the hangman game! 😁") # initial welcome message
main_hangman_game() # start the main game loop