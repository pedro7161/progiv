import time

# ex1
count = 0
vogais = 0
Twords = 0
words_t = []
try:
    with open('ficha12.txt') as f:
        lines = f.readlines()


except:
    print('Problema na abertuta do ficheiro')


# ex2
words_t = []
unique = []
try:
    with open('ficha12.txt') as f:
        lines = f.readlines()
    f.close()
except:
    print('Problema na abertuta do ficheiro')

for text in lines:
    str = text

    words_t.append(str.split(" "))

for line in range(len(words_t)):
    for word in range(len(words_t[line])):
        if words_t[line][word] != "\n" and words_t[line][word] not in unique:
            unique.append(words_t[line][word])
        else:
            continue

try:
    f = open('ficha12_newtext.txt', 'x')
    print("creating file...")
    time.sleep(5)
    f.close()
except:
    print('Problema na criaçao do ficheiro')


try:
    with open('ficha12_newtext.txt', 'r+') as f:
        lines = f.readlines()

except:
    print('Problema na abertuta do ficheiro')

for word in range(len(unique)):
    f.write(unique[word])
f.close()
