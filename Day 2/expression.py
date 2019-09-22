# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:42:30 2019

@author: SUMEDH
"""
x = float(input("Enter x : "))
y = float(input("Enter y : "))
result = (x+y)**2
if result.is_integer():
    print("(x+y)^2 = ", int(result))
else:
    print("(x+y)^2 = ", result)
