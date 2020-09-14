# -*- coding: utf-8 -*-
#!urs/bin/env pythn3



def listToString(list):
    str1 = ""  
    for ele in list:  
        str1 += ele    
    return str1 
count = 0
list = input("Enter the string: ").split()
string = listToString(list)
duplicates = []
for char in string:
   if string.count(char) > 1:
       if char not in duplicates:
           duplicates.append(char)
           count = count +1
print(*duplicates)
print("Number of Element Repeated is: " + str(count))

	