# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:36:59 2019

@author: SUMEDH
"""

print("_____________Nth multiple of K in Fibonacci_____________")
n = int(input("Enter n : "))
k = int(input("Enter k : "))

MAX = 1000

def getPosition(n, k):
    fib1 = 0
    fib2 = 1
    for i in range(2,MAX):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        if fib2%k == 0:
            return n*i
    return
  
print(getPosition(n,k))