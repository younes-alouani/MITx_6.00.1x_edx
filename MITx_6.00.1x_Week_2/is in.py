# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    
    if aStr == "" :
        return False
    if len(aStr) <= 2 : 
        if char == aStr[0] :
            return True
        if char == aStr[1] :
            return True
        else :
            return False
    elif char == aStr[(len(aStr))//2 +1] :
        return True
    elif char < aStr[(len(aStr))//2 +1] :
        return isIn(char, aStr[:(len(aStr))//2 +1])
    elif char > aStr[(len(aStr))//2 + 1] :
        return isIn(char, aStr[(len(aStr))//2 +1:])
    