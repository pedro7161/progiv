from enum import Enum
class imparpar(Enum):
    PAR=0
    IMPAR=1
def checkpar(list,p):
  
    lista=[]
    for num in list:
        if num%2==p:
            lista.append(num)
    return lista
def converter(text):
    lista2=[]
    lista=text.split(",")
    for n in lista:
        lista2.append(int(n))
    return tuple(checkpar(lista2,imparpar.PAR.value))

def mult(nums,multiplayer):
    arr=[]
    for n in nums:
        if n%multiplayer==0:
            arr.append(n)
    return arr

print(converter(input("digite um tuplo")))


numeros = (10,15,3,6,99,45,63,30,344,22,4,25,10)

print("A) ",len(numeros))
print("B) ",max(numeros),min(numeros))
numeros2 = (21, 53, 23, 54,22,2,1,13)
numeros3=numeros+numeros2
print("C) ",numeros3)

print("D) ",checkpar(numeros3,imparpar.IMPAR.value))
multiplayer=5
print("E) ",mult(numeros3,multiplayer))




