def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = len(aStr)//2
    if char == "" and aStr == "":
        return True
    elif char == "" or aStr == "":
        return False
    elif aStr[mid] == char:
        return True
    elif aStr[mid] < char:
        return isIn(char, aStr[mid+1:])
    else:
        return isIn(char, aStr[:mid])