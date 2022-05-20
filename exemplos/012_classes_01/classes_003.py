  
# classes_003
 
# Com os métodos setters e getters 
# Os setters e getters permitem definir e obter dados dos atributos

class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
	 
	def setNome(self, nome):
		self.nome= nome
	
	def getNome(self):
		return self.nome

	def setIdade(self, idade):
		self.idade= idade
	
	def getIdade(self):
		return self.idade

	
pess1 = Pessoa('ana silva', 25)

print('Nome:', pess1.nome);
print('Idade:', pess1.idade)

pess2 = Pessoa('marco gomes', 23)
print('Nome:', pess2.nome);

pess2.setNome('Ivo Reis')

print('Nome:', pess2.nome);
print('Idade:', pess2.idade)









