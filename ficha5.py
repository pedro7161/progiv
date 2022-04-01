def ex1(C): 
    return C * 1.8 + 32
def ex2(arr2):
    x=sorted(arr2)
    return  "o valor intermedio: ",x[1]
def ex3(n1):
    if n1%1==0 and n1%n1==0:
        return "1"
    else:
        return "0"

print(ex1(float(input("digite celcius: "))))

arr2=[]
n1=int(input("digite num: "))
n2=int(input("digite num: "))
n3=int(input("digite num: "))
arr2.append(n1)
arr2.append(n2)
arr2.append(n3)
print(ex2(arr2))

n1=2
print(ex3(n1))

numeros = [1,5,3,6,22,45,63,30,344,22,12,25,10]
# a) Apresenta o comprimento da lista.
# b) Apresenta o máximo e mínimo da lista.
# c) Acrescenta ao final da lista os elementos da lista:
# numeros2 = [21,53,23,54,22,2,1,13]
# d) Altera a lista numeros por forma a que fique ordenada.
# e) Indica qual o elemento que aparece mais, indicando o índice da primeira
# ocorrência na lista.
# f) Imprime os elementos da lista numa só linha e separados por “-”.
# g) Imprime os elementos de índice ímpar.
# h) Imprime os elementos que são múltiplos de 5.