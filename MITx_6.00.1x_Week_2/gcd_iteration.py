# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a >= b :
        max_gcd = b
    if a < b :
        max_gcd = a                   

    while a % max_gcd != 0 or b % max_gcd != 0 :
        max_gcd -= 1
              
    return max_gcd
    
    
 
        
    