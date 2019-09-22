# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:55:53 2019

@author: SUMEDH
"""
principalAmount = float(input("Enter the principal amount : "))
intrestRate = float(input("Enter pcpa : "))
numOfYears = int(input("Enter Time period : ")) 
compoundIntrest = principalAmount*(((1 + (intrestRate/100))**numOfYears) - 1.0)
print('Compound Intrest = ',round(compoundIntrest,2))
