  
# class para uma calculadora para realizar operações aritméticas básicas

class calc:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def soma(self):
		return self.x + self.y
	def subtrair(self):
		return self.x - self.y
	def multiplicar(self):
		return self.x * self.y
	def dividir(self):
		return self.x / self.y
 
	
calc1 =  calc(20,  30)
print(calc1.soma())
print(calc1.subtrair())
print(calc1.multiplicar())
print(calc1.dividir())
