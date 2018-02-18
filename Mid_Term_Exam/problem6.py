#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:32:22 2018

@author: muiky
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N == 0 :
        return 0
    return N % 10 + sumDigits(N//10)