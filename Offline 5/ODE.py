import numpy as np
import matplotlib.pyplot as plt

pi = 3.1416
def f(x,y):
    return (x+20*y)*(np.sin(x*y))

def euler(xi, yi, h):
    return yi + h*f(xi,yi)

def RK_2nd(xi, yi, a2, h):
    a1 = 1 - a2
    p1 = 0.5/a2
    q11 = 0.5/a2
    
    k1 = f(xi, yi)
    k2 = f(xi + p1*h, yi + q11*k1*h)
    return yi + (a1*k1 + a2*k2)*h

def huen(xi, yi, h):
    return RK_2nd(xi, yi, 0.5, h)

def midpoint(xi, yi, h):
    return RK_2nd(xi, yi, 1, h)

def ralston(xi, yi, h):
    return RK_2nd(xi, yi, 2/3, h)

def RK_4th(xi,yi,h):
    k1 = f(xi, yi)
    k2 = f(xi + 0.5 * h, yi + 0.5*k1*h)
    k3 = f(xi + 0.5*h, yi +0.5*k2*h)
    k4 = f(xi + h, yi + k3*h)
    return yi + (k1+2*k2+2*k3+k4)*(1/6)*h
    

x1=[]
x2=[]
x3=[]
x4=[]
y1=[]
y2=[]
y3=[]
y4=[]
y=[]
yhuen=[]
ymidpoint=[]
yralston=[]
yrk4th=[]
x=[]
y1.append(4)
y2.append(4)
y3.append(4)
y4.append(4)

for i in np.arange(0, 10+0.01, 0.01):
    x1.append(i)
for i in np.arange(0, 10+0.05, 0.05):
    x2.append(i)
for i in np.arange(0, 10+0.1, 0.1):
    x3.append(i)
for i in np.arange(0, 10+0.5, 0.5):
    x4.append(i)
    
for i in range(1, len(x1)):
    y1.append(euler(x1[i-1], y1[i-1], 0.01))
for i in range(1, len(x2)):
    y2.append(euler(x2[i-1], y2[i-1], 0.05))
for i in range(1, len(x3)):
    y3.append(euler(x3[i-1], y3[i-1], 0.1))
for i in range(1, len(x4)):
    y4.append(euler(x4[i-1], y4[i-1], 0.5))
plt.figure(figsize=(15,10))
plt.plot(x1,y1, label="h=0.01")
plt.plot(x2,y2, label="h=0.05")
plt.plot(x3,y3, label="h=0.1")
plt.plot(x4,y4, label="h=0.5")
plt.title("EULER METHOD")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()


y1.clear()
y2.clear()
y3.clear()
y4.clear()


y1.append(4)
y2.append(4)
y3.append(4)
y4.append(4)

for i in range(1, len(x1)):
    y1.append(huen(x1[i-1], y1[i-1], 0.01))
for i in range(1, len(x2)):
    y2.append(huen(x2[i-1], y2[i-1], 0.05))
for i in range(1, len(x3)):
    y3.append(huen(x3[i-1], y3[i-1], 0.1))
for i in range(1, len(x4)):
    y4.append(huen(x4[i-1], y4[i-1], 0.5))
plt.figure(figsize=(15,10))
plt.plot(x1,y1, label="h=0.01")
plt.plot(x2,y2, label="h=0.05")
plt.plot(x3,y3, label="h=0.1")
plt.plot(x4,y4, label="h=0.5")
plt.title("HUEN METHOD")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

y1.clear()
y2.clear()
y3.clear()
y4.clear()


y1.append(4)
y2.append(4)
y3.append(4)
y4.append(4)

for i in range(1, len(x1)):
    y1.append(midpoint(x1[i-1], y1[i-1], 0.01))
for i in range(1, len(x2)):
    y2.append(midpoint(x2[i-1], y2[i-1], 0.05))
for i in range(1, len(x3)):
    y3.append(midpoint(x3[i-1], y3[i-1], 0.1))
for i in range(1, len(x4)):
    y4.append(midpoint(x4[i-1], y4[i-1], 0.5))
plt.figure(figsize=(15,10))
plt.plot(x1,y1, label="h=0.01")
plt.plot(x2,y2, label="h=0.05")
plt.plot(x3,y3, label="h=0.1")
plt.plot(x4,y4, label="h=0.5")
plt.title("MIDPOINT METHOD")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

y1.clear()
y2.clear()
y3.clear()
y4.clear()


y1.append(4)
y2.append(4)
y3.append(4)
y4.append(4)

for i in range(1, len(x1)):
    y1.append(ralston(x1[i-1], y1[i-1], 0.01))
for i in range(1, len(x2)):
    y2.append(ralston(x2[i-1], y2[i-1], 0.05))
for i in range(1, len(x3)):
    y3.append(ralston(x3[i-1], y3[i-1], 0.1))
for i in range(1, len(x4)):
    y4.append(ralston(x4[i-1], y4[i-1], 0.5))
plt.figure(figsize=(15,10))
plt.plot(x1,y1, label="h=0.01")
plt.plot(x2,y2, label="h=0.05")
plt.plot(x3,y3, label="h=0.1")
plt.plot(x4,y4, label="h=0.5")
plt.title("RALSTON METHOD")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

y1.clear()
y2.clear()
y3.clear()
y4.clear()

y1.append(4)
y2.append(4)
y3.append(4)
y4.append(4)


for i in range(1, len(x1)):
    y1.append(RK_4th(x1[i-1], y1[i-1], 0.01))
for i in range(1, len(x2)):
    y2.append(RK_4th(x2[i-1], y2[i-1], 0.05))
for i in range(1, len(x3)):
    y3.append(RK_4th(x3[i-1], y3[i-1], 0.1))
for i in range(1, len(x4)):
    y4.append(RK_4th(x4[i-1], y4[i-1], 0.5))
plt.figure(figsize=(15,10))
plt.plot(x1,y1, label="h=0.01")
plt.plot(x2,y2, label="h=0.05")
plt.plot(x3,y3, label="h=0.1")
plt.plot(x4,y4, label="h=0.5")
plt.title("RK 4TH METHOD")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()


x.clear()
y.clear()
yhuen.clear()
ymidpoint.clear()
yralston.clear()
yrk4th.clear()

y.append(4)
yhuen.append(4)
ymidpoint.append(4)
yralston.append(4)
yrk4th.append(4)
for i in np.arange(0, 10+0.01, 0.01):
    x.append(i)
for i in range(1, len(x)):
    y.append(euler(x[i-1], y[i-1], 0.01))
    yhuen.append(huen(x[i-1], yhuen[i-1], 0.01))
    ymidpoint.append(midpoint(x[i-1], ymidpoint[i-1], 0.01))
    yralston.append(ralston(x[i-1], yralston[i-1], 0.01))
    yrk4th.append(RK_4th(x[i-1], yrk4th[i-1], 0.01))
plt.figure(figsize=(15,10))
plt.plot(x,y, label="EULER")
plt.plot(x,yhuen, label="HUEN")
plt.plot(x,ymidpoint, label="MIDPOINT")
plt.plot(x,yralston, label="RALSTON")
plt.plot(x,yrk4th, label="RK 4TH")
plt.title("h=0.01")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

plt.figure(figsize=(15,10))

x.clear()
y.clear()
yhuen.clear()
ymidpoint.clear()
yralston.clear()
yrk4th.clear()

y.append(4)
yhuen.append(4)
ymidpoint.append(4)
yralston.append(4)
yrk4th.append(4)
for i in np.arange(0, 10+0.05, 0.05):
    x.append(i)
for i in range(1, len(x)):
    y.append(euler(x[i-1], y[i-1], 0.05))
    yhuen.append(huen(x[i-1], yhuen[i-1], 0.05))
    ymidpoint.append(midpoint(x[i-1], ymidpoint[i-1], 0.05))
    yralston.append(ralston(x[i-1], yralston[i-1], 0.05))
    yrk4th.append(RK_4th(x[i-1], yrk4th[i-1], 0.05))
plt.plot(x,y, label="EULER")
plt.plot(x,yhuen, label="HUEN")
plt.plot(x,ymidpoint, label="MIDPOINT")
plt.plot(x,yralston, label="RALSTON")
plt.plot(x,yrk4th, label="RK 4TH")
plt.title("h=0.05")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

plt.figure(figsize=(15,10))
x.clear()
y.clear()
yhuen.clear()
ymidpoint.clear()
yralston.clear()
yrk4th.clear()

y.append(4)
yhuen.append(4)
ymidpoint.append(4)
yralston.append(4)
yrk4th.append(4)

for i in np.arange(0, 10+0.1, 0.1):
    x.append(i)

for i in range(1, len(x)):
    y.append(euler(x[i-1], y[i-1], 0.1))
    yhuen.append(huen(x[i-1], yhuen[i-1], 0.1))
    ymidpoint.append(midpoint(x[i-1], ymidpoint[i-1], 0.1))
    yralston.append(ralston(x[i-1], yralston[i-1], 0.1))
    yrk4th.append(RK_4th(x[i-1], yrk4th[i-1], 0.1))
plt.plot(x,y, label="EULER")
plt.plot(x,yhuen, label="HUEN")
plt.plot(x,ymidpoint, label="MIDPOINT")
plt.plot(x,yralston, label="RALSTON")
plt.plot(x,yrk4th, label="RK 4TH")
plt.title("h=0.1")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

plt.figure(figsize=(15,10))
x.clear()
y.clear()
yhuen.clear()
ymidpoint.clear()
yralston.clear()
yrk4th.clear()

y.append(4)
yhuen.append(4)
ymidpoint.append(4)
yralston.append(4)
yrk4th.append(4)

for i in np.arange(0, 10+0.5, 0.5):
    x.append(i)
    
for i in range(1, len(x)):
    y.append(euler(x[i-1], y[i-1], 0.5))
    yhuen.append(huen(x[i-1], yhuen[i-1], 0.5))
    ymidpoint.append(midpoint(x[i-1], ymidpoint[i-1], 0.5))
    yralston.append(ralston(x[i-1], yralston[i-1], 0.5))
    yrk4th.append(RK_4th(x[i-1], yrk4th[i-1], 0.5))
plt.plot(x,y, label="EULER")
plt.plot(x,yhuen, label="HUEN")
plt.plot(x,ymidpoint, label="MIDPOINT")
plt.plot(x,yralston, label="RALSTON")
plt.plot(x,yrk4th, label="RK 4TH")
plt.title("h=0.5")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
