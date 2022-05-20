
# Classe Circulo

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return (math.pi * (self.raio * self.raio))
    def perimetro(self):
        return (2 * math.pi * self.raio)

circ1 = Circulo(5)
print('Area do Circulo 1 = ', circ1.area())
print('Perimetro do Circulo 1 = ', circ1.perimetro())

circ2 = Circulo(7)
print('Area do Circulo 2 = ', circ2.area())
print('Perimetro do Circulo 2 = ', circ2.perimetro())

