# dictionary of photos that shows thw player's state
HANGMAN_PHOTOS = {0: """x-------x""",
                  1: """x-------x
|
|
|
|
|""",
                  2: """x-------x
|       |
|       0
|
|
|""",
                  3: """x-------x
|       |
|       0
|       |
|
|""",
                  4: """x-------x
|       |
|       0
|      /|\\
|
|""",
                  5: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
                  6: """ x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}

# ascii art for start screen
HANGMAN_ASCII_ART = """Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/\n"""

# the max tries a player has
MAX_TRIES = 6


def check_win(secret_word, old_letters_guessed):
    """Checks if the player won the game.
        :param secret_word: the word that the player needs to guess
        :param old_letters_guessed: a list that contains all the letters the player guessed
        :type secret_word: string
        :type old_letters_guessed: list
        :return: The result for checking if the player won the game
        :rtype: bool
        """
    # we assume that the player has won
    win_flag = True

    # going over each letter in the secret word
    for letter in secret_word:
        # if the letter was not guessed by player, he did not win
        if letter not in old_letters_guessed:
            # we switch the flag to False because the letter was not guessed by player
            win_flag = False

    # we return the flag with answer
    return win_flag


def show_hidden_word(secret_word, old_letters_guessed):
    """Shows the word that needs to be guessed with letters the player already guessed.
        :param secret_word: the word that the player needs to guess
        :param old_letters_guessed: a list that contains all the letters the player guessed
        :type secret_word: string
        :type old_letters_guessed: list
        :return: prints the word with letters that were guessed
        :rtype: null
        """
    new_word = ""

    # going over each letter in the secret word
    for letter in secret_word:
        # if the letter was guessed by player, we can show it
        if letter in old_letters_guessed:
            new_word += letter + ' '
        # if the letter wasn't guessed, we show the player _ instead of letter
        else:
            new_word += '_ '
    # show player the secret word
    print(new_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the letter that was guessed is valid.
        :param letter_guessed: the letter that the player guessed
        :param old_letters_guessed: a list that contains all the letters the player guessed
        :type letter_guessed: string
        :type old_letters_guessed: list
        :return: The result for checking if the letter is valid
        :rtype: bool
        """
    # if the input length is bigger than one, then not valid
    if len(letter_guessed) > 1:
        return False

    # if the input is not an alphabet letter, then not valid
    elif not letter_guessed.isalpha():
        return False

    # if the player already guessed the letter , then not valid
    elif letter_guessed in old_letters_guessed:
        return False

    # if the letter passed the checks above, then is valid
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Updating the list of guessed letters if the letter is valid.
        :param letter_guessed: the letter that the player guessed
        :param old_letters_guessed: a list that contains all the letters the player guessed
        :type letter_guessed: string
        :type old_letters_guessed: list
        :return: The result for succeeding to update the list
        :rtype: bool
        """
    # first we lower the letter that was guessed
    letter_guessed = letter_guessed.lower()

    # checking if the letter is valid
    if check_valid_input(letter_guessed, old_letters_guessed):
        # if the letter is valid, we add it to the letter guessed list
        old_letters_guessed.append(letter_guessed)
        # return True because we succeed to append list
        return True
    # if the letter didn't pass the valid check
    else:
        print("X")
        # sort the list of letters that were guessed
        old_letters_guessed.sort()
        # print the letter that was guessed
        print(" -> ".join(old_letters_guessed))
        # return False because we failed to append list
        return False


def choose_word(file_path, index):
    """Choosing a word to play with from file according to given index.
        :param file_path: a path to a file with words
        :param index: an index to choose a word with
        :type file_path: string
        :type index: int
        :return: The secret word to play with
        :rtype: string
        """

    # opening file with given path to read
    file_words = open(file_path, "r")
    # read data from file
    data = file_words.read()
    # creating a list of words from file
    words = data.split(" ")
    # create a new list that will be with no dupes
    without_dupes = []

    # going over every word in file
    for word in words:
        # if we did not add the word to new list than add it
        if word not in without_dupes:
            without_dupes.append(word)

    # if we get index bigger than the length of the list
    while index >= len(words):
        # new index is from start of list
        index -= len(words)

    # return word to play with
    return words[index - 1]


def print_hangman(num_of_tries):
    """Printing the state of the hangman according to the amount of guesses.
        :param num_of_tries: the amount of guesses the player made
        :type num_of_tries: int
        :return: print the state of the hangman
        :rtype: null
        """
    # print the state of the hangman
    print(HANGMAN_PHOTOS[num_of_tries])


def print_welcome_screen(max_tries):
    """Printing the welcome screen for player.
        :param max_tries: the maximum guesses the player has
        :type max_tries: int
        :return: print the welcome screen for player
        :rtype: null
        """
    # print welcome message
    print(HANGMAN_ASCII_ART, max_tries)


def main():
    # Initializes the number of tries to 0
    num_of_tries = 0

    # Creates an empty list to store guessed letters
    old_letters_guessed = []

    # Prints the welcome screen with a specified maximum number of tries.
    print_welcome_screen(MAX_TRIES)

    # Asks the user to input the file path containing words and the index to select a word.
    file_words = input("Enter file path: ")
    index_word = int(input("Enter index: "))

    # Chooses a secret word from the file based on the provided index.
    secret_word = choose_word(file_words, index_word)

    # Prints a message to indicate the start of the game.
    print("Let's start!")

    # Prints the initial state of the hangman.
    print_hangman(num_of_tries)

    # Displays the hidden version of the secret word.
    show_hidden_word(secret_word, old_letters_guessed)

    # Initializes a flag to track if the player has won the game.
    win_flag = False

    # Enters a loop to allow the player to guess letters until they win or run out of tries.
    while (win_flag is not True) and (num_of_tries < MAX_TRIES):

        # Asks the user to guess a letter.
        letter = input("Guess a letter: ")

        # Checks if the guessed letter is valid and updates the list of guessed letters.
        if try_update_letter_guessed(letter, old_letters_guessed):

            # Increments the number of tries if the guessed letter is valid.
            num_of_tries += 1

            # Checks if the guessed letter is in the secret word.
            if letter in secret_word:
                # Checks if the player has guessed all letters in the word.
                if check_win(secret_word, old_letters_guessed):
                    # Prints a message that the player has won.
                    print("WIN")
                    # Updates the win flag to True to exit the loop.
                    win_flag = True
            else:
                # Prints a message to indicate an incorrect guess and shows the hangman display.
                print(":(")
                print_hangman(num_of_tries)

            # Displays the hidden version of the secret word with updated guessed letters.
            show_hidden_word(secret_word, old_letters_guessed)

    # Prints "LOSE" if the player used all tries without guessing the word.
    print("LOSE")


if __name__ == '__main__':
    main()
