# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:06:38 2020

@author: chinm
"""

def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
        
n = int(input("Enter the number of layers to be printed: "))
pyramid(n)
            