# -*- coding: utf-8 -*-
"""
oddTuples is a procedure that takes a tuple. And stores the elements whose the index is odd in a new tuple 
input : tuple
output : tuple
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    tuple = ()
    for i in range(0,len(aTup)) :
        if i % 2 == 0 :
            tuple = tuple + (aTup[i],)
    return tuple
