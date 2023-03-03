def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    x = 0
    if x == 0:
        char = "".join(sorted(aStr))
        lower = 0
        upper = len(aStr)
        x+=1
    ans = (lower+upper)//2
    if char == aStr[ans]:
        return True
    else:
        if char > aStr:
            lower = ans
        else: 
            upper = ans
        return isIn(char, aStr)
print(isIn("a", "abcd"))
        