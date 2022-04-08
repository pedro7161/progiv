from random import random


import random
def ex1(arr):
    sum=0
    for n in arr:
        if n>20:
            sum=sum+n
    return sum
def ex2(arr):
    ar=[]
    count=0
    for i in range(0,4):  
        for k in range(0,3):
            if arr[i][k]<0:
                ar.append(arr[i][k])
                count+=1
    print(ar)
    return "quantidade de negativos: ", count

arr=[]
for i in range(0,5):
    arr.append(float(input("digite um valor: ")))
print(ex1(arr))

arr2=[[1,3,4],
      [5,6,7],
      [8,9,10],
      [11,12,13]]

for i in range(0,4):  #faz de 0-3 ou seja 3 (0,1,2)
    for k in range(0,3): #faz de 0-4 ou seja 4 (0 1 2 3)
        r=random.randint(-100,100)
        arr2[i][k]=r
print(arr2)
print(ex2(arr2))