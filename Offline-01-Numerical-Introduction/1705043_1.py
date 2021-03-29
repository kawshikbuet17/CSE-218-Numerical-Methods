# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy
import matplotlib.pyplot as plt

def func_ln_onePLUSx(x,n):
    sum = 0
    for i in range(1,n+1):
        sign = (-1)**(i+1)
        temp = (x**i)/i
        temp = sign*temp    
        sum = sum + temp
    return sum

print("Make a test of your written function")
x = input("Input the value of x : ")
n = input("Input the value of n : ")

x = float(x)
n = int(n)

print("Where x = ", x , ",n = ", n, "Value of ln(1+x) is : ",func_ln_onePLUSx(x,n))
print()
print()
print("Here is the graph of ln(1+x)")
list1 = []
list2 = []
list3 = []



plt.figure(figsize=(10,10))
plt.grid("True")
plt.xlabel("value of x")
plt.ylabel("value of ln(1+x)")

for i in numpy.arange(-1+0.1, 1, 0.1):
    list1.append(i)
    
for i in list1:
    list2.append(math.log(1+i))
    
plt.plot(list1, list2, label="Builtin Log")

for i in list1:
    list3.append(func_ln_onePLUSx(i,1))
plt.plot(list1,list3, label="iteration=1")
list3.clear()
for i in list1:
    list3.append(func_ln_onePLUSx(i,3))
plt.plot(list1,list3, label="iteration=3")
list3.clear()
for i in list1:
    list3.append(func_ln_onePLUSx(i,5))
plt.plot(list1,list3, label="iteration=5")
list3.clear()
for i in list1:
    list3.append(func_ln_onePLUSx(i,20))
plt.plot(list1,list3, label="iteration=20")
list3.clear()
for i in list1:
    list3.append(func_ln_onePLUSx(i,50))
plt.plot(list1,list3, label="iteration=50")
list3.clear()
plt.legend()
plt.show()

print()
print()
print("Here is the graph of relative error")
plt.figure(figsize=(10, 10))
plt.xlabel("value of n")
plt.ylabel("Relative error")
list4 = []
list5 = []
for i in range(1,51):
    list5.append(i)
for i in range(1, 51):
    list4.append(abs((math.log(1.5)-func_ln_onePLUSx(0.5,i))))
plt.plot(list5, list4)
plt.grid("True")
#plt.legend()
plt.show()





