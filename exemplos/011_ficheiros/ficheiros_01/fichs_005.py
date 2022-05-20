 
# r+ abre o ficheiro para leitura e escrita

fo = open('info.txt', 'r+')

str = fo.readline()

print(str)

fo.write('O Rio Tejo') 
fo.close()


