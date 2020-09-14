# -*- coding: utf-8 -*-
#!#!/usr/bin/python3


def reverse_string(s):
    k=[]
    l=[]
    for i in range(len(s)):
        if(s[i]==" "):
            l.append(i)
        else:
            k.append(s[i])
    k.reverse()
    
    for i in range(len(l)):
        k.insert(l[i]," ")
    a = "".join(k)
    print(a)
    return a
  
    return l
s=input()
new_string = reverse_string(s)

if(s==new_string):
    print("String {} is a Palindrome".format(s))
else:
    print("String {} is not a Palindrome".format(s))
    


