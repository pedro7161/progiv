# ex1
numeros = [1,5,3,6,22,45,63,30,344,22,12,25,10]
numeros.reverse()
print("A) ",numeros)
numeros.sort()
print("B) ",numeros)
print("C) ",numeros[-3:])
# ex2
str=input("digite um frase:")
subs=input("Digite uma substring a ser substituída:")
new=input("Digite uma substring de substituição:")
if str.find(subs)==-1:
    print("nao foi encontrado a palavra: ",subs)

str=str.replace(subs,new)
print(str)