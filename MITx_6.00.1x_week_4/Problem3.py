def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    actualHand = eval(repr(hand))
    isInWordList = (word in wordList)
    isWordInHand = True
    if word == "" :
        return False
    for letter in word :
        if actualHand.get(letter,0) > 0 :
            isWordInHand = (isWordInHand and True)
            actualHand[letter] -= 1
        else :
            isWordInHand = (isWordInHand and False)
            break
    return (isWordInHand and isInWordList)


            
            
                