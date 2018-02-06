# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# variabless

left = 0
right = 100
guess = 50
response = "l"

#Start message
print("Please think of a number between 0 and 100!")

#Bisection loops
while response != "c" :
    while True :
        print("Is your secret number "+ str(guess)+"?")
        response = input("Enter 'h' to indicate the guess is too high. "
                         "Enter 'l' to indicate the guess is too low. "
                         "Enter 'c' to indicate I guessed correctly. ")
        if response in "hlc" :
            break
        else : print("Sorry, I did not understand your input.")
    
    if response == "h" :
        right = guess
        guess = (right + left) // 2
        
    
    if response == "l" :
        left = guess
        guess = (right + left) // 2
        
    
print("Game over. Your secret number was: ",guess)
    
    
 
        
    