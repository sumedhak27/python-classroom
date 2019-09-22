# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:34:24 2019

@author: SUMEDH
"""

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(a,b))