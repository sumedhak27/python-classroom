# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:27:04 2019

@author: SUMEDH
"""

a = float(input("Enter first number : "))
b = float(input("Enter second number : ")) 
sumation = a+b
if sumation.is_integer():
    print("The sum is = ",int(a+b))
else:
    print("The sum is = ",a+b)
