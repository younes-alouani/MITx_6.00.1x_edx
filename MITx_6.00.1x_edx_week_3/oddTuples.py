def isWordGuessed(secretWord, lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    guessedWord = ""  
    for letter in secretWord :    
        if (letter in lettersGuessed) :
            guessedWord += letter
        else :
            guessedWord += "_ "
    
    return guessedWord == secretWord
    