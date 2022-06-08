import random
# Importing the function choose_word from the file words.py
from words import choose_word
# Importing the list of images from the file images.py
from images import hangman_images


def is_word_guessed_right(secret_word, letters_guessed):
    """
    It takes the secret word and the letters guessed and returns True if the secret word is guessed and False if it is not yet.
    
    :param secret_word: word to be guessed by the user
    :param letters_guessed: list holds all the words guessed by the user
    :return: True or False
    """
    
    secret_word = sorted(list(set(secret_word)))
    letters_guessed = sorted(letters_guessed)

    result = True
    for x in secret_word:
        if x in letters_guessed:
            pass
        else:
            result = False
    return result

    """
    Alternative(slightly more optimized) :
    for x in secret_word:
        if x not in letters_guessed:
            return False
    return True
    """


def get_guessed_word(secret_word, letters_guessed):
    """
    It takes the secret word and a list of letters guessed by the user and returns a string with the
    letters guessed correctly and underscores for the letters not guessed yet.
     
    :param secret_word: word to be guessed by the user.
    :param letters_guessed: list holds all the words guessed by the user.

    Example :- 
        > If secret_word -> "kindness" and letters_guessed = [k, n, s]
            return "k_n_n_ss"
    """
    
    index = 0
    user_guessed_word = ""
    
    while(index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            user_guessed_word += secret_word[index]
        else:
            user_guessed_word += "_"
        index += 1

    return user_guessed_word
    

def get_available_letters(letters_guessed):
    """
    It takes a list of letters guessed and returns a string of all the letters that haven't been guessed yet.
    
    :param letters_guessed: list contains all guessed characters

    Returns: 
        It returns a string which contains all letters except the already guessed ones.

    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting -> `bcdfghijklmnopqrstuvwxyz`
    """
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets = set(alphabets)    
    letters_guessed = set(letters_guessed)
    
    letters_left = sorted(list(alphabets - letters_guessed))
    letters_left = "".join(letters_left)
    return letters_left


def display_image(image_index):
    """
    It takes in an integer as an argument and returns the corresponding image from the list of hangman
    images
    
    :param image_index: The index of the image to display
    :return: The image_index is being returned.
    """
    return hangman_images[image_index]


def hint(secret_word, letters_guessed):
    """
    It takes the secret word and the list of letters guessed, and returns a random character from the secret word that hasn't been guessed yet
    
    :param secret_word: string, the word the user is guessing; assumes all letters are
    :param letters_guessed: list, what letters have been guessed so far
    :return: A random character from the list of letters_not_guessed
    """

    letters_not_guessed = []
    for character in secret_word:
        if character not in letters_guessed:
            letters_not_guessed.append(character)
            
    random_character = random.choice(letters_not_guessed)
    return random_character
    

# Driver Function
def hangman(secret_word):
    # 8 tries to guess the right word
    remaining_lives = 8
    # Player can only use the hint once
    hint_count = 1
    
    '''
    secret_word(string) : Word to be guessed by the user.

    Steps to start Hangman :
    > In the beginning of the game, user will know about the total characters in the secret_word.
    > In each round, user will guess one character.
    > After each character give a feedback to the user :
        * Right or wrong
        * Display partial word guessed by the user and use underscore in place of unguessed characters.    
    '''
    
    print("Welcome to the Hangman Game !")
    print("\nI am thinking of a word that is {} letters long.".format(str(len(secret_word))), end = '\n\n')
        
    # Creating an empty list to store the letters guessed by the user.
    letters_guessed = []
    # This is the main loop of the game. It will keep running until the user either guesses the word, uses the hint more than once or runs out of lives.

    print("User, kindly enter the letters of your choice one at a time. If at any point, you feel the need of using a hint, type 'hint'. Note : The hint can only be used once.")
    while((remaining_lives != 0) and (hint_count >= 0)):
        user_choice = input("User's Input : ")
        user_choice = user_choice.lower()
            
        if user_choice in secret_word:
            # Adding the user's input to the list of letters guessed.
            letters_guessed.append(user_choice)
            print("Good Guess!!! : {} ".format(get_guessed_word(secret_word, letters_guessed)))
            
            available_letters = get_available_letters(letters_guessed)
            print("Available letters : {} ".format(available_letters))   
            
            if is_word_guessed_right(secret_word, letters_guessed):
                print(" *** Congratulations, you won !!! Very well played *** ", end = '\n\n')
                break   
            
        elif user_choice == "hint":
            hint_count -= 1
            # Appending the hinted letter to the list of letters guessed.
            letters_guessed.append(hint(secret_word, letters_guessed))
            print("Hint Used ! : {}".format(get_guessed_word(secret_word, letters_guessed)))
            
            available_letters = get_available_letters(letters_guessed)
            print("Available Letters: {} ".format(available_letters))   
            
            if is_word_guessed_right(secret_word, letters_guessed):
                print(" *** Congratulations, you won !!! Very well played *** ", end = '\n\n')
                break
            
        else:
            print("Oops! That letter is not in my word : {} ".format(get_guessed_word(secret_word, letters_guessed)))
            # Adding the user's input to the list of letters guessed.
            letters_guessed.append(user_choice)
            
            available_letters = get_available_letters(letters_guessed)
            print("\nAvailable Letters : {} ".format(available_letters)) 
            print("\n")
  
            # Printing the hangman image.
            print(display_image(8 - (remaining_lives)))
                               
            remaining_lives -= 1
            print("Remaining Lives :", remaining_lives)
            continue
        
    if (remaining_lives == 0):
        print("*** Game Over, Better Luck Next Time!!! :) ***")
        print("Correct word was : ", secret_word)
        

# Calling the function choose_word() from the file words.py and assigning the return value to the variable secret_word.
secret_word = choose_word()
# Calling the function hangman() and passing the secret_word as an argument.
hangman(secret_word)