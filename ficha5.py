import math


def ex1(C):
    return C * 1.8 + 32


def ex2(arr2):
    x = sorted(arr2)
    return "o valor intermedio: ", x[1]


def ex3(n1):
    if n1 % 1 == 0 and n1 % n1 == 0:
        return "1"
    else:
        return "0"


print(ex1(float(input("digite celcius: "))))

arr2 = []
n1 = int(input("digite num: "))
n2 = int(input("digite num: "))
n3 = int(input("digite num: "))
arr2.append(n1)
arr2.append(n2)
arr2.append(n3)
print(ex2(arr2))

n1 = 2
print(ex3(n1))

numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]

print("A) ", len(numeros))
print("B) max: ", max(numeros), "min: ", min(numeros))
numeros2 = [21, 53, 23, 54, 22, 2, 1, 13]
for n in numeros2:
    numeros.append(n)
print("C) ", numeros)
numeros.sort()
print("D) ", numeros)

before = 0
num = numeros[0]
for n in numeros:
    now = numeros.count(n)
    if now > before:
        before = now
        num = n
print("E) ", num)
print("F) ")
for n in numeros:
    print(n, "-", end="")

for n in numeros:
    if n % 2 != 0:
        print("G) n impar: ", n)
    if n % 5 == 0:
        print("H) multiplo de 5: ", n)
