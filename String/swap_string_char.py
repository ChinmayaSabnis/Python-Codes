# -*- coding: utf-8 -*-
#!urs/bin/env python3



def changech(str1,ch1,ch2):
    result = ""
    if str1 != None:
        result = str1.replace(ch1, '*').replace(ch2,ch1).replace('*', ch2)
        return result
    return 'Null'

str1 = input()
ch1,ch2 = map(str,input().split())
print(changech(str1,ch1,ch2))

