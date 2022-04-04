import math
soma = 0
i = 20
for k in range(i, 0, -2):
    soma += k
print('Soma =', soma)

lista1 = ["Iva", 25, "Rui", 19, "Rato", "abc", 33]

print(lista1)

print(lista1[2:5])
print(lista1[:3])   
print(lista1[3:])   
lista2= ["jose", 25, "catia", 19, "gato", "xyz", 33]
lista2.append(lista1)
print(lista2)


def ex3_esfera(r):
    return (4*math.pi*math.pow(r,3))/3

print(ex3_esfera(5))

a=int(input("digite um numero: "))

for k in range(1,a+1):
    print("*"*k)