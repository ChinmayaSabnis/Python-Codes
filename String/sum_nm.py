# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:44:48 2020

@author: chinm
"""


n =int(input("N:"))
m =int(input("M:"))


def calculate(n ,m):
    sum_nm =0
    for i in range(n,m+1,1):
        if i%3 == 0 and i%5 == 0:
            sum_nm = sum_nm + i
    print(sum_nm)

calculate(n, m)
