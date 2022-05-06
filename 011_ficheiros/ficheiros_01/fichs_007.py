 
# file.tell() retorna a posição corrente no ficheiro
# file.seek() posiciona-se no ficheiro (ex. posicionar-se no 6º carater)

fo = open('info.txt', 'r')

fo.seek(6)
 
str = fo.read()

k = fo.tell()

print(str)

print('A posição corrente no ficheiro = ', k)

fo.close()






