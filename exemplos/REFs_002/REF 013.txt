import math

# Calculo da média de 7 valores de temperaturas
# digitados para uma lista-array

nums = []

for k in range (0,7):
    nums.append(float(input("Numero: ")))

media = sum(nums) / len(nums)

print("\n Media das Temperaturas: ", media)


# outra forma de fazer - a clássica

soma = 0
for k in range (0,7):
    soma = soma + nums[k]

media = soma / len(nums)

print("\n A mesma Média - metodo classico: ", media)




