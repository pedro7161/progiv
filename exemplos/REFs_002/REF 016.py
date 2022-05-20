
'''
Crie um programa que determine qual o valor máximo de uma tabela
bidimensional 4X3 de floats, através de uma função por si criada.
Deve criar o array com valores digitados do tipo float e passá-lo
como argumento à função.
O resultado deve ser impresso pelo programa chamante.
'''

nums = [ [10.0, 20.0, 30.0], [40.0, 50.0, 60.0], [12.0, 99.0, 20.0],
         [13.8, 14.6, 18.5]]

def calcMax(lista):
    val_max = lista[0][0]
    for i in range(4):
        for j in range(3):
            if (lista[i][j] > val_max):
                val_max = lista[i][j]
    return val_max

print(calcMax(nums))

           