# -*- coding: utf-8 -*-
#!urs/bin/env pythn3

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
    print("".join(k))
    
s = ""
s=input()
reverse_string(s)
