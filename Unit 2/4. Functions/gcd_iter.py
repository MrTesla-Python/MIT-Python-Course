def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        x = a
    else:
        x = b
    if a == b:
        return a
    while x > 0:
        if a%x==0 and b%x == 0:
            return x
        else:
            x-=1
print(gcdIter(17, 12))