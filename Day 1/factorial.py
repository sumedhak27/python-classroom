# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:34:57 2019

@author: SUMEDH
"""

print("............Factorial Program...........")
inputNumber = int(input("Enter input number : "))

def factorial(num):
    factorial = 1;
    for x in range(1,num+1):
        factorial *= x
    return factorial

print('The factorial of ', inputNumber, ' is ', factorial(inputNumber))