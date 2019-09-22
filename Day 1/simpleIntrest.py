# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:43:12 2019

@author: SUMEDH
"""

amount = float(input("Enter the Amount in Rs : "))
intrestRate = float(input('Enter the intrest rate per year (pcpa): '))
numOfYears = int(input('Enter number of years : '))

simpleIntrest = ((amount*intrestRate)/100)*numOfYears
totalAmountAfterIntrest = amount + simpleIntrest

print('Simple intrest = ',simpleIntrest)
print('Total amount after intrest = ', totalAmountAfterIntrest)
