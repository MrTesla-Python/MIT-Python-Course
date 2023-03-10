SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    word_value = 0
    for i in word:
        word_value += SCRABBLE_LETTER_VALUES[i]
    word_value = word_value * len(word)
    if len(word) == n:
        word_value+=50
    return word_value
print(getWordScore("weed", 7))

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    ans = hand.copy()
    for i in word:
        if i in ans.keys():
            ans[i]-=1
    return ans
    
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

print(updateHand(hand, "quailll"))

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    word_dict = getFrequencyDict(word)
    if word in wordList:
        if len(word_dict) > len(hand):
            return False
        for key in word_dict.keys():
            if key not in hand.keys():
                return False
            elif word_dict[key] > hand[key]:
                return False
        return True
    else:
        return False

WORDLIST_FILENAME = "C:/Users/trist/OneDrive/Documents/GitHub/MIT-Python-Course/Unit 4/Problem Set 4/words.txt"
print(isValidWord("F", hand, WORDLIST_FILENAME))