# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:58:09 2019

@author: SUMEDH
"""
fib = [1,1]

def getNthFibonacciNumber(n):
    if n == 1 or n == 2:
        return fib[n-1]
    else :
        for i in range(len(fib),n):
            fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

n = int(input("Enter the number : "))
            
print(getNthFibonacciNumber(n))

''' is number fibonacci or not '''
fib = [1,1]
def isfibonacci(num):
    while fib[-1] < num :
        fib.append(fib[-1] + fib[-2])
    if num in fib:
        print(num, ' is a fibonacci number.')
    else:
        print(num, ' is not a fibonacci number.')
        
checkNumber = int(input("Enter number under fibonacci test : "))

isfibonacci(checkNumber)

        
