#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:52:18 2018

@author: muiky
"""
def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    L_copy = []
    for i in L:
        if g(f(i)) == True:
            L_copy.append(i)
    L[:] = L_copy
    if len(L) == 0:
        return -1
    else:
        return max(L)



L = [555,555]
print(applyF_filterG(L, f, g))
print(L)
