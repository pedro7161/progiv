  
# classes_009 com dado protected

# Um dado ou método protected somente pode ser acedido
# pela própria classe ou pela classes derivadas.

class Pessoa:
	def __init__(self, nome, idade):
		self._nome = nome # dado protected
		self.idade = idade
	
	def setNome(self, nome):
		self._nome = nome
	
	def getNome(self):
		return self._nome

	def setIdade(self, idade):
		self.idade= idade
	
	def getIdade(self):
		return self.idade
 
pess1 = Pessoa('ana silva', 25)
print('Nome objeto pess1 de Pessoa:', pess1.getNome());
print('Idade objeto pess1 de Pessoa:', pess1.idade)

# Herança
class medico(Pessoa):
	def __init__(self, numOrdem, nome, idade):
		 Pessoa.__init__(self, nome, idade)
		 self.numOrdem=numOrdem
	def mostra(self):
		return self._nome
	
		 
m = medico(12345, 'rui', 40)
print('Nome objeto m de medico:', m.getNome())
print('Idade objeto m de medico:', m.idade)
print('Numero da Ordem objeto m de medico:', m.numOrdem)
print(m.mostra())





