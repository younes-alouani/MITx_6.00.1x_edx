#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:06:38 2018

@author: muiky
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    total = 0
    try :
        for i in range(0,len(listA)) :
            total += listA[i] * listB[i]
    except :
        total = 0
    return total