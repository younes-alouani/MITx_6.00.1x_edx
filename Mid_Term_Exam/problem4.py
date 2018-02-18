#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:33:55 2018

@author: muiky
"""
def lessThan4(aList):
    '''
    input :: aList: a list of strings
    output :: bListMax4: a list of strings
    '''
    bListMax4 = []
    for word in aList :
        if len(word) < 4 :
            bListMax4 += [word]
    return bListMax4
            