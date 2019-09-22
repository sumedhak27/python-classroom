# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:32:17 2019

@author: SUMEDH
"""
import math
print('............Distance Calculation between two points..........')
inputString = input('Enter x1,y1 and x2,y2 (space seperated):')
x1,y1,x2,y2 = map(int,inputString.split())
distance  = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
print('Distance = ',distance)