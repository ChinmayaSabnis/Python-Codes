# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:35:48 2020

@author: chinm
"""


def OperationChoices(c,a,b):
    if c == 1:
        return (a + b)
    elif c == 1:
        return (a + b)
    elif c == 3:
        return (a * b)
    elif c == 4:
        return (a / b)
    
c,a,b = map(int,input().split())

print(OperationChoices(c, a, b))