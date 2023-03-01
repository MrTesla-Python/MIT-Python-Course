# Hangman game
import random
import string
alph = string.ascii_lowercase

WORDLIST_FILENAME = "C:/Users/trist/OneDrive/Documents/GitHub/MIT-Python-Course/Unit 3/Problem Set 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count+=1
    if count == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ""
    for i in secretWord:
        if i in lettersGuessed:
            guessed += i
        else: 
            guessed += "_"
    return guessed.strip()

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)

    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    guesses = 8
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    lettersGuessed = []
    print("-----------------------------")
    while isWordGuessed(secretWord,lettersGuessed) == False:
        
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        newLetter = input("Please guess a letter: ")
        if newLetter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(newLetter.lower())
            if newLetter in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
        print("-----------------------------")
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            quit()
    print("Congratulations, you won!")
        

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)