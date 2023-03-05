def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    tup = ()
    for t in range(len(aTup)):
        if t%2==0:
            tup = tup + (aTup[t],)
    return tup