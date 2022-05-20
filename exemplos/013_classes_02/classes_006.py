  
# class para uma calculadora para somar

class calc:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def soma(self):
		return self.x + self.y

calc1 =  calc(20,  30)

print(calc1.soma())

 