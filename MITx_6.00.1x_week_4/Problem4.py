def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    Handlen = 0    
    for i in hand :
        Handlen += hand[i]
    return Handlen


            
            
                