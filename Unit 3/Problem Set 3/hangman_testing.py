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
            guessed += " _ "
    return guessed.strip()

print(getGuessedWord("apple", ["a", "c", "e"]))

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

print(isWordGuessed("apple", ["a", "c", "e", "p", "", "l", "e"]))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in letters:
        if i in lettersGuessed:
            letters.remove(i)
    return "".join(letters)
print(getAvailableLetters(["a", "c", "e", "p", "", "l", "e"]))