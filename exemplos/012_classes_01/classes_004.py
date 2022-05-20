  
# classes_004
# Outro exemplo dos getters e setters
 
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
pess2.setNome('ivo reis')
print('Nome:', pess2.nome);
print('Idade:', pess2.idade)

pess1.setNome('lia ana')
pess1.setIdade(25)

print('Nome:', pess1.getNome());
print('Idade:', pess1.getIdade())

print('Nome:', pess1.nome)






