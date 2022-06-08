import random

def load_words():
    """
    This function takes a file name as input and returns a list of all the words in the file
    :return: list of words
    """
        
    file = open("words.txt", 'r')
    word_list = file.readline().split(" ")
    return word_list


def choose_word():
    """
    This function takes a list of words and returns a random word from the list.
    :return: A random word from the list of words.
    """
        
    list_of_all_words = load_words()
    secret_word = random.choice(list_of_all_words)
    return secret_word