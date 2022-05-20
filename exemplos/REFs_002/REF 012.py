
'''
Escreva em Python um programa que receba do teclado uma lista de inteiros 
e devolva uma lista contendo apenas os algarismos pares (não levando assim 
em consideração os restantes elementos). 

Exemplo de utilização: 
Insira uma lista de inteiros positivos: 1, 6, 7, 99, 56 

Resposta:
Algarismos pares: [6, 56]

Nota:
O tamanho da lista deve ser pedido ao utilizador para digitar
'''

lista1 = []

num = int(input('Digite quantos valores deseja introduzir: '))

print("Introduza os valores: ")

for i in range(num):
    k = int(input("Valor: "))
    if k % 2 == 0:
        lista1.append(k)

print("Os numeros pares são: ", lista1)
  
    






