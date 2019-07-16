def nonNegative(list):
    flag = 1
    for i in range(len(list[0])):
        if list[0][i] < 0:
            flag = 0
            break
    
    if flag==1:
        return True
    else:
        return False

def index_j_Define(list, n, m):
    index_j = 0
    min_x = list[0][0]
    for i in range(n+m):
        if min_x>list[0][i]:
            min_x = list[0][i]
            index_j = i
    return index_j
    

def intercept(list, n, m):
    index_j = index_j_Define(list, n, m)
    for i in range(1,m+1):
        try:
            list[i][n+m+1] = list[i][n+m]/list[i][index_j]
        except:
            list[i][n+m+1] = 10000000000

def lowest_Intercept(list, n, m):
    intercept(list, n, m)
    index_i=1 
    min = 10000000000
    for i in range(1, m+1):
        if list[i][n+m+1]>0:
            if min>list[i][n+m+1] :
                min = list[i][n+m+1]
                index_i = i
    return index_i
        

def solving_By_Simplex_Method(list, n, m):
    index_i = lowest_Intercept(list, n, m)
    index_j = index_j_Define(list, n, m)
    
    divisor = list[index_i][index_j]
    for i in range(n+m+1):
        list[index_i][i] = list[index_i][i]/divisor
    
    for i in range(m+1):
        temp = list[i][index_j]/list[index_i][index_j]
        for j in range(n+m+1):
            if i != index_i:
                list[i][j] = list[i][j]-temp*list[index_i][j]
    lowest_Intercept(list, n, m)
    return list

def value_of_x(list, n, m):
    xlist=[0 for i in  range(n)]
    for i in range(n):
        for j in range(1,m+1):
            if list[j][i]==1:
                xlist[i] = list[j][n+m]
    return xlist
                

f = open("in2.txt", "r")

commands = []
count = 0
while True:
    line = f.readline()
    if line == "":
        break
    else:
        commands.append(line)
        count+=1

m = count-1
list = []
list = [float(j) for j in commands[0].split()]
n = len(list)
mainlist = [[0 for i in range(n+m+2)]for j in range(m+1)]

for i in range(n):
    mainlist[0][i] = -list[i]

for i in range(m):
    list.clear()
    list = [float(k) for k in commands[i+1].split()]
    for j in range(n):
        mainlist[i+1][j] = float(list[j])
    mainlist[i+1][n+m] = list[-1]

for i in range(m):
    mainlist[i+1][n+i] = 1
f.close()

while nonNegative(mainlist)==False:
    a = solving_By_Simplex_Method(mainlist, n, m)
    for i in range(m+1):
        for j in range(n+m+1):
            print(str(round(a[i][j], 2)), end=' \t')
        print()
    print()


print("Highest value of Z is : ", mainlist[0][n+m])
x = value_of_x(a, n, m)
for i in range(len(x)):
    indx = i+1
    print("x"+str(indx)+" is \t"+str(x[i]))
