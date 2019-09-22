# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 23:09:02 2019

@author: SUMEDH
"""
char = input("Enter a character : ")
while len(char) != 1:
    print('Error!! Only one charcter is allowed.')
    char = input("Enter a character : ")

print('ASCII value of ',char, ' is', ord(char))