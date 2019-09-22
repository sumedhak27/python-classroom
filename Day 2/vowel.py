# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:27:58 2019

@author: SUMEDH
"""
#vowel or not

vowels = ['a','e','i','o','u','A','E','I','O','U']

inp = input("Enter the character: ")

for i in range(0,):
    if len(inp) != 1:
        inp = input("Enter the character: ")

if(inp in vowels):
    print(inp, " is vowel.")
else:
    print(inp, "is not a vowel.")