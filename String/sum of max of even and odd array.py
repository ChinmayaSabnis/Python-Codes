# -*- coding: utf-8 -*-
#!urs/bin/env pythn3


array=[]
evenarr = []
oddarr =[]

n = int(input("Enter the size of array:"))
for i in range(0,n):
    num = int(input("Enter the element at index {}:" .format(i)))
    array.append(num)
    if num%2==0:
        evenarr.append(array[i])
    else:
        oddarr.append(array[i])

evenarr = sorted(evenarr)
oddarr = sorted(oddarr)

evnmax=max(evenarr)
oddmax = max(oddarr)
print("Even Array is: {} ".format(evenarr))
print("Odd Array is: {} ".format(oddarr))

i = len(evenarr)
j = len(oddarr)
if i!=0 and j!= 0:
    sum_ = evenarr[i-1] + oddarr[j-1]
    print("Sum of max element of even and odd array is: " + str(sum_))
else:
    print("Empty Array Found!")