# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:20:30 2019

@author: SUMEDH
"""
import math
radius = float(input('Enter the radius: '))
def areaOfCircle(rad):
    return math.pi*(radius**2) 
print('Area Of Circle  = ',areaOfCircle(radius))