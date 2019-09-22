# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:10:39 2019

@author: SUMEDH
"""

inputNum = input("Enter the input number : ")
cubeSum = 0
for x in inputNum:
    cubeSum += int(x)**3
    
if cubeSum == int(inputNum):
    print(inputNum, ' is a armstrog number.')
else:
    print(inputNum, ' is NOT a armstrog number.')