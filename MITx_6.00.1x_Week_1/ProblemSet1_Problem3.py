# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

substring = s[0]
for g_index in range(len(s)) :
    
    temp = s[g_index]
    l_index = g_index
    
    if l_index == len(s) - 1 :
            break
    
    while s[l_index] <= s[l_index+1] :
        temp = temp + s[l_index+1]
        l_index += 1
        
        if len(substring) < len(temp) :
            substring = temp
            
        if l_index == len(s) - 1 :
            break
        
    
print("Longest substringstring in alphabetical order is: ",substring)
    
    
 
        
    