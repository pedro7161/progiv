 
# leitura de todas as linhas de um ficheiro
# e imprimir o ficheiro em forma de lista

fo = open('info.txt', 'r')

str = fo.readlines()
 
print(str)
fo.close()
