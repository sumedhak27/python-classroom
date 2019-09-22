# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:52:40 2019

@author: SUMEDH
"""

weight, height = map(float,input('Enter weight in kg and height in m : ').split())
bmi = weight / (height**2)
print('BMI = ',bmi)