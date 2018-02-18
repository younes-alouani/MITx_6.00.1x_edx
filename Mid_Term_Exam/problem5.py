#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:49:29 2018

@author: muiky
"""
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    dic_rev
    '''
    #create a new empty dic 
    dic_rev = dict()
    #reverse key_values but initializing values to empty list
    for key in d :
        if d[key] not in dic_rev :
            dic_rev[d[key]] = []
    
    #regroup keys having same value
    for key in d :
        dic_rev[d[key]] += [key]
        
    #sort the elements :
    for key in dic_rev :
        dic_rev[key] = sorted(dic_rev[key])
        
    return dic_rev