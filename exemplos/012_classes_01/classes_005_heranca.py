  
# classes_005_heranca

'''
Herança de classes
A herança é a característica que as linguagens de programação 
orientadas por objectos apresentam, a qual lhes permite derivar 
novas classes de classes já existentes.

Tal como uma bola de futebol é um tipo de bola, uma pessoa 
é um tipo de mamífero e uma laranja é um tipo de fruto, etc.
Assim podemos derivar uma classe de outra à qual chamamos 
superclasse.

Ao declararmos uma classe podemos derivá-la, conforme abaixo ilustrado:

'''
 
class Pessoa:
	def __init__(self, nome='', idade=0):
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
print('Nome objeto pess1 de Pessoa:', pess1.nome);
print('Idade objeto pess1 de Pessoa:', pess1.idade)

pess2 = Pessoa('marco gomes', 23)
print('Nome objeto pess2  de Pessoa:', pess2.nome);
print('Idade objeto pess2 de Pessoa:', pess2.idade)

pess3 = Pessoa()
pess3.setNome('lia ana')
pess3.setIdade(25)

print('Nome objeto pess3 de Pessoa:', pess3.getNome());
print('Idade objeto pess3 de Pessoa:', pess3.getIdade())


# Herança
# Nota:
# É necessário chamar o construtor da classe base
# para inicializar os atributos herdados, já que 
# uma classe herdada não herda os construtores da 
# classe base

class medico(Pessoa):
        def __init__(self, numOrdem, nome, idade):
                Pessoa.__init__(self, nome, idade) 
                self.numOrdem=numOrdem

m = medico(12345, 'rui', 40)
print('Nome objeto m de medico:', m.nome)
print('Idade objeto m de medico:', m.idade)
print('Numero da Ordem objeto m de medico:', m.numOrdem)













