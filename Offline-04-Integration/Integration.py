import numpy as np
import matplotlib.pyplot as plt


def trapezoidal(a,b,fa,fb):
    return (b-a)*(fa+fb)/2

def simpson_ONE_by_THREE(a,b,fx0,fx1,fx2):
    return (b - a) * (fx0 + 4*fx1 + fx2) / 6

def simpson_THREE_by_EIGHT(a,b,fx0,fx1,fx2,fx3):
    return (b - a) * (fx0 + 3*fx1 + 3*fx2 +fx3) / 8


f = open("data1.txt", "r")
string = f.readline()
n = int(string)

xy= []
x = []
y = []

for i in range(n):
    string = f.readline()
    xy.append(string.split())
for i in range(n):
    x.append(float(xy[i][0]))
    y.append(float(xy[i][1]))
        
f.close()



plt.figure(figsize=(15,10))
plt.scatter(x,y)
plt.plot(x,y)

sol = 0
i=0
v1=1
v2=1
v3=1
trapezoid=0
one_by_three=0
three_by_eight=0

while i<n-1:

    ai=i
    temp = x[i+1]-x[i]
    c=0
    var=i
    for j in range(var,n-1):
        if round(x[i+1]-x[i],5)==round(temp,5):
            c+=1
            i+=1
            
    bi=i
    if c==1:
        sol += trapezoidal(x[ai], x[ai+1], y[ai], y[ai+1])
        if v3==1:
            plt.fill_between(x[ai:ai+2], y[ai:ai+2], color="LIGHTPINK", label="trapezoidal")
            v3=0
        else:
            plt.fill_between(x[ai:ai+2], y[ai:ai+2], color="LIGHTPINK")
        trapezoid+=1
        
    elif c%3==0:
        c3 = c//3
        while c3:
            sol += simpson_THREE_by_EIGHT(x[ai], x[ai+3], y[ai], y[ai+1], y[ai+2], y[ai+3])
            if v1==1:
                plt.fill_between(x[ai:ai+4], y[ai:ai+4], color="MEDIUMPURPLE", label="simpson 3/8 rule")
                v1=0
            else:
                plt.fill_between(x[ai:ai+4], y[ai:ai+4], color="MEDIUMPURPLE")
            c3-=1
            ai=ai+3
            three_by_eight+=3
    else:
        if (c%3)%2==0:
            
            
            c3 = c//3
            while c3:
                sol += simpson_THREE_by_EIGHT(x[ai], x[ai+3], y[ai], y[ai+1], y[ai+2], y[ai+3])
                if v1==1:
                    plt.fill_between(x[ai:ai+4], y[ai:ai+4], color="MEDIUMPURPLE", label="simpson 3/8 rule")
                    v1=0
                else:
                    plt.fill_between(x[ai:ai+4], y[ai:ai+4], color="MEDIUMPURPLE")
                c3-=1
                ai=ai+3
                three_by_eight+=3
            
            c=c%3
            c2 = c//2
            
            while c2:
        
                sol += simpson_ONE_by_THREE(x[ai], x[ai+2], y[ai], y[ai+1], y[ai+2])
                if v2==1:
                    plt.fill_between(x[ai:ai+3], y[ai:ai+3], color="LIGHTSKYBLUE", label="simpson 1/3 rule")
                    v2=0
                else:
                    plt.fill_between(x[ai:ai+3], y[ai:ai+3], color="LIGHTSKYBLUE")
                c2-=1
                ai=ai+2
                one_by_three+=2
        else:
            c3 = (c-3)//3
            c3_b = c3
            while c3:
                sol += simpson_THREE_by_EIGHT(x[ai], x[ai+3], y[ai], y[ai+1], y[ai+2], y[ai+3])
                if v1==1:
                    plt.fill_between(x[ai:ai+4], y[ai:ai+4], color="MEDIUMPURPLE", label="simpson 3/8 rule")
                    v1=0
                else:
                    plt.fill_between(x[ai:ai+4], y[ai:ai+4], color="MEDIUMPURPLE")
                c3-=1
                ai=ai+3
                three_by_eight+=3
                
            c = c-c3_b*3
            c2 = c//2
        
            while c2:
                sol += simpson_ONE_by_THREE(x[ai], x[ai+2], y[ai], y[ai+1], y[ai+2])
                if v2==1:
                    plt.fill_between(x[ai:ai+3], y[ai:ai+3], color="LIGHTSKYBLUE", label="simpson 1/3 rule")
                    v2=0
                else:
                    plt.fill_between(x[ai:ai+3], y[ai:ai+3], color="LIGHTSKYBLUE")
                c2-=1
                ai=ai+2
                one_by_three+=2

plt.grid("True")
plt.xlabel("X value")
plt.ylabel("Y value")
plt.title("Integration")
plt.legend()

print("Trapezoid:",trapezoid,"intervals")
print("1/3 rule:", one_by_three, "intervals")
print("3/8 rule:", three_by_eight, "intervals")
print()
print("Integral value:", sol)
