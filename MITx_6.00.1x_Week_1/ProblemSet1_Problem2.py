# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

index = 0
bob_number =0
for char in s :
    if index + 3 <= len(s) :
        if char == "b" and s[index+1] == "o" and s[index+2] == "b":
            bob_number += 1
    index += 1
print("Number of times bob occurs is: ",bob_number)
    
    
 
        
    