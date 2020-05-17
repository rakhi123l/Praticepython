# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:07:41 2020

@author: admin
"""

import string
alpha = string.ascii_lowercase

n = int(input())
L = []

for i in range(n):
    s = "-".join(alpha[i:n])
    L.append(s[::-1]+s[1:])

width = len(L[0])

for i in range(n-1, 0, -1):
    print(L[i].center(width, "-"))

for i in range(n):
    print(L[i].center(width, "-"))
    

s = 'the brown fox'
lst = [word[0].upper() + word[1:] for word in s.split()]
print(lst)
s = " ".join(lst)
print(s)