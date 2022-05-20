'''
 Apresenta algumas primitivas dos arrays, tais como,
 len(), max() e min() na realização de alguns cálculos
''' 
import math

vals = [14, 20, 12, 30, 18]

print('Num elementos: ', len(vals))
 
print('Valor Maximo: ', max(vals))

print('Valor Minimo: ', min(vals))

print(vals)

media = sum(vals) / len(vals)
print("A média é: " + str(round(media, 2)))
