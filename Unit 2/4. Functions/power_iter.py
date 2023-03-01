def iterPower(base, exp):
    ans = 1
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1.0
    else:
        while exp > 0:
            ans = ans * (base)
            exp -= 1