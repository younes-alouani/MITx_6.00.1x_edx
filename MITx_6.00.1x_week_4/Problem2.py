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
    assert type(word) == str, "word is not a string"
    assert type(hand) == dict, "hand is not a dict"
    updatedHand = eval(repr(hand))
    for letter in word :
        updatedHand[letter] -= 1
    return updatedHand


            
            
                