# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:27:37 2019

@author: SUMEDH
"""
startInteval = int(input("Enter the start number : "))
endInterval = int(input("Enter the end number : "))

primeNumbersArray = [1]*(endInterval+1)

for i in range(2,endInterval+1):
    if primeNumbersArray[i] == 1:
        if i > startInteval:
            print(i)
        for j in range(i, endInterval+1, i):
            primeNumbersArray[j] = 0