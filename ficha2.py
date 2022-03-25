import math
def ex1(a):
    if a<=20 and a>=0:
        return "nota valida"
    else:
        return "nota invalida"

def ex2(c):
    return c * 1.8 + 32
def ex3(n1):
    
    if n1<=0:
        return "nao pode ser 0 nem negativo. termina o programa"
    else:
        n1-=1
        for n1 in range(n1,0,-1):
            print(n1)
        return "sucesso"
def ex4(raio):
    # 2 * π * Raio
    return "o perimetro e: ", 2*math.pi *raio
print(ex1(int(input("escreva uma nota entre 0-20"))))

for i in range(10,20):
    print(ex2(i))

print(ex3(int(input("digite um numero"))))
print(ex4(int(input("digite um numero"))))