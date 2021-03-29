# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 21:40:11 2019

@author: ASUS
"""

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
    return upper, lower, y, x


def validity(upper, n):
    for i in range(n):
        flag=0
        for j in range(n):
            if upper[i][j]==0:
                flag+=1
        if flag == n:
            return False
    return True
    


f = open("in1.txt", "r")
string = f.readline()
n = int(string)

mat = [[0 for i in range(n)]for j in range(n)]
b = [0 for i in range(n)]

for i in range(n):
    string = f.readline()
    mat[i] = [float(j) for j in string.split()]
        
for i in range(n):
    string = f.readline()
    b[i] = float(string)
f.close()
upper, lower, solvey, solvex = get_Solution(mat, n, b)

fout = open("out1.txt", "w")


for i in range(n):
    for j in range(n):
        fout.write(str(round(lower[i][j], 4))+' ')
        #fout.write(str.format('{0:.4f}', lower[i][j]))
        #fout.write(' ')
    fout.write("\n")
fout.write("\n")

for i in range(n):
    for j in range(n):
        fout.write(str(round(upper[i][j], 4))+' ')
        #fout.write(str.format('{0:.4f}', upper[i][j]))
        #fout.write(' ')
    fout.write("\n")
fout.write("\n")  

if validity(upper, n)==True:
    for i in range(n):
        fout.write(str(round(solvey[i], 4))+"\n")
        #fout.write(str.format('{0:.4f}', solvey[i]))
        #fout.write("\n") 
    fout.write("\n") 
    for i in range(n):
        fout.write(str(round(solvex[i],4))+"\n")   
        #fout.write(str.format('{0:.4f}', solvex[i]))
        #fout.write("\n") 
    fout.close()
else:
    fout.write("No unique solution")