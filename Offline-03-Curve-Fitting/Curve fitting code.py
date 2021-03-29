# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:28:56 2019

@author: ASUS
"""
import numpy as np
import matplotlib.pyplot as plt



def S_x_POW_n(listx, n):
    sum = 0 
    for i in listx:
        sum = sum + np.power(i,n)
    return sum

def S_x_POW_n_y_POW_m(n,x,y,px,py):
    sum=0
    for i in range(n):
        sum+=(x[i]**px)*(y[i]**py)
    return sum

def LU_decomposition(mat, n):
    lower = [[0 for i in range(n)]for j in range(n)]
    upper = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            lower[i][j]=0
            upper[i][j]=0
    
    for i in range(n):
        for k in range(i,n):
            sum = 0
            for j in range(i):
                sum = sum + lower[i][j] * upper[j][k]
            upper[i][k]=mat[i][k]-sum
        
        for k in range(i,n):
            if(i != k):
                sum=0
                for j in range(i):
                    sum = sum + lower[k][j]*upper[j][i]
                lower[k][i] = (mat[k][i]-sum)/upper[i][i]
            else:
                lower[i][i]=1
    return lower, upper


def get_Solution(mat, n, b):
    lower, upper = LU_decomposition(mat, n)
    y = [0 for i in range(n)]
    x = [0 for i in range(n)]
    
    for i in range(n):
        sum=0
        for p in range(i):
            sum = sum + lower[i][p]*y[p]
        y[i] = (b[i]-sum)/lower[i][i]
    
    for i in range(n-1, -1, -1):
        sum = 0
        for p in range(n-1, i, -1):
            sum = sum + upper[i][p]*x[p]
        x[i] = (y[i]-sum)/upper[i][i]
    return x

def LinearRegression(m, n, listx, listy):
    matrix = [[0 for i in range(m+1)] for j in range(m+1)]
    
    for i in range(m+1):
        for j in range(m+1):
            matrix[i][j] = S_x_POW_n(listx, i+j)
    
    B = [0 for i in range(m+1)]
    for i in range(m+1):
        B[i] = S_x_POW_n_y_POW_m(n, listx, listy, i, 1)

    
    a = get_Solution(matrix, m+1, B)
    #a = np.linalg.solve(matrix,B)
    return a

def Regression_Coefficient(listx, listy, n, m):
    yTotal = 0
    for i in range(n):
        yTotal += listy[i]
    yAvg = yTotal/n
    
    St = 0
    for i in range(n):
        St = St + (listy[i] - yAvg)**2
        
    Sr = 0
    for i in range(n):
        temp = 0
        for j in range(m+1):
            temp += a[j]*(listx[i]**j)
        Sr = Sr + (listy[i]-temp)**2
    
    r = (St - Sr)/St
    r = r**0.5
    return r
    


file = open("data.txt", "r")
commands = []
count = 0
while True:
    line = file.readline()
    if line == "":
        break
    else:
        commands.append(line)
        count+=1
listxy = []
listx = []
listy = []
for i in range(len(commands)):
    listxy.append(commands[i].split())
    listx.append(float(listxy[i][0]))
    listy.append(float(listxy[i][1]))
listx = np.array(listx)
listy = np.array(listy)
plt.figure(figsize=(15,10))
plt.scatter(listx, listy, s=2)



m=1
n= count
a = LinearRegression(m, n, listx, listy)
ynew = []
for i in range(n):
    y=0
    for j in range(m+1):
        y = y+a[j]*(np.power(listx[i], j))
    ynew.append(y)
print("Parameters of Order", m, ":")
for i in range(m+1):
    print("a"+str(i)+" =",round(a[i],4))
print("regression coefficient of order",m, "is", Regression_Coefficient(listx, listy, n, m))
print()
x = [i for i in listx]
for i in range(n):
    for j in range(n-i-1):
        if x[j+1]>x[j]:
            x[j+1], x[j] = x[j], x[j+1]
            ynew[j+1], ynew[j] = ynew[j], ynew[j+1]
plt.plot(x, ynew, label="Order 1")



m=2
n= count
a = LinearRegression(m, n, listx, listy)
ynew.clear()
for i in range(n):
    y=0
    for j in range(m+1):
        y = y+a[j]*(np.power(listx[i], j))
    ynew.append(y)
print("Parameters of Order", m, ":")
for i in range(m+1):
    print("a"+str(i)+" =",round(a[i],4))
print("regression coefficient of order",m,"is",Regression_Coefficient(listx, listy, n, m))
print()
x = [i for i in listx]
for i in range(n):
    for j in range(n-i-1):
        if x[j+1]>x[j]:
            x[j+1], x[j] = x[j], x[j+1]
            ynew[j+1], ynew[j] = ynew[j], ynew[j+1]

plt.plot(x, ynew, label="Order 2")



m=3
n= count
a = LinearRegression(m, n, listx, listy)
ynew.clear()
for i in range(n):
    y=0
    for j in range(m+1):
        y = y+a[j]*(np.power(listx[i], j))
    ynew.append(y)
print("Parameters of Order", m, ":")
for i in range(m+1):
    print("a"+str(i)+" =",round(a[i],4))
print("regression coefficient of order",m,"is", Regression_Coefficient(listx, listy, n, m))
print()

x = [i for i in listx]
for i in range(n):
    for j in range(n-i-1):
        if x[j+1]>x[j]:
            x[j+1], x[j] = x[j], x[j+1]
            ynew[j+1], ynew[j] = ynew[j], ynew[j+1]
plt.plot(x, ynew, label="Order 3")
plt.grid("True")
plt.legend()
