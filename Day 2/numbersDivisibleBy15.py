# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:03:49 2019

@author: SUMEDH
"""
numList = list(map(float, input('Enter space saperated numbers : ').split()))
print(list(filter(lambda x: x%15 == 0,numList)))
