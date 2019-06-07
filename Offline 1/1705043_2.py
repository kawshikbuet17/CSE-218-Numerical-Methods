# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:16:26 2019

@author: ASUS
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    f = x**3 - 2400*(x**2) - 3*x +2
    #f = (x/(1-x))*((6/(2+x))**0.5)-0.05
    return f

def falsePosition(func, a, b, TOL, N):
    i=1
    FA = func(a)
    
    while(i<=N):
        x = (a*func(b)-b*func(a))/(func(b)-func(a))
        FP = func(x)
        
        if(FP==0 or np.abs(func(x))<TOL):
            break
        
        i = i+1
        
        if(FA*FP>0):
            a = x
        else:
            b = x
    return x,i

def secant(func, x0, x1, TOL, N):
    f_x0 = func(x0)
    f_x1 = func(x1)
    i = 0
    while abs(f_x1) > TOL and N>0:
        if(f_x1 - f_x0)/(x1 - x0)==0:
            print("Denominator zero")
        x = x1 - (f_x1)*(x1-x0)/(f_x1-f_x0)
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = func(x1)
        i += 1
        N-=1
    if abs(f_x1) > TOL:
        i = -1
    return x, i

a = 0
b = 1
result1, step1 = falsePosition(func, a, b, 0.005, 10000)
print("Result from False Position Method : ", result1)
print("Iteration number of False Position Method : ", step1)

result2, step2 = secant(func, a, b, 0.005, 10000)
print("Result from Secant Method : ", result2)
print("Iteration number of Secant Method : ", step2)

list1 =[]
list2 =[]
for i in np.arange(-500, 2500, 0.01):
    list1.append(i)
    list2.append(func(i))
plt.figure(figsize=(10,10))
plt.grid("True")

plt.plot(list1, list2)
plt.show()
    

