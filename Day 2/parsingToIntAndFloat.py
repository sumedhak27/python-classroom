# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:42:28 2019

@author: SUMEDH
"""

print("Parsing a string to Int and Float.")
intStr = input('Enter the Integer string : ')
floatStr = input('Enter the Flo1 2 at string : ')
intList =  list(map(int,intStr.split()))
floatList =  list(map(float,floatStr.split()))
print(intList, floatList)
