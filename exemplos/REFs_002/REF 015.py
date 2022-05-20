
'''
Crie um programa que determine a soma dos elementos de uma tabela
bidimensional 4X3 de floats, através de uma função por si criada.

Crie a tabela.

O resultado deve ser impresso pelo programa chamante.
'''

nums = [ [10.0, 20.0, 30.0], [40.0, 50.0, 60.0], [12.0, 99.0, 20.0],
         [13.8, 14.6, 18.5]]

def calcSoma(lista):
    soma = 0
    for i in range(4):
        for j in range(3):
            soma = soma + lista[i][j]
    return soma

print(calcSoma(nums))

            
