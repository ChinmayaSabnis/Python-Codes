# -*- coding: utf-8 -*-
#!usr/bin/env python3

def pyramid(n):
    num = 0
    for i in range(0,n):
        num =1
        for j in range(0,i+1):
            print(num,end="")
            num = num+1
        print("\r")
        
n = int(input("Enter the number of layers to be printed: "))
pyramid(n)
           

