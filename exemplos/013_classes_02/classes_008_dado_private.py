  
# classes_008 com dado private

''' 
Data member private

Somente podem ser acedidos a partir de dentro da 
própria classe.

A partir de fora da classe, os dados private somente
podem ser acedidos através de métodos públicos da
classe que servem assim de interface entre os dados 
private da classe e os objetos interessados no seu
acesso.

Estes métodos de interface têm o nome genérico de
getters e setters.

Nota:
Quando o especificador de acesso não é especificado
então os dados são public.

Aliás, em Python, tudo (classes, variáveis e métodos)
são public por defeito.

'''

class Pessoa:
	def __init__(self, nome, idade):
		self.__nome = nome # dado private
		self.idade = idade
	
	def setNome(self, nome):
		self.__nome = nome
	
	def getNome(self):
		return self.__nome

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

		 
m = medico(12345, 'rui', 40)
print('Nome objeto m de medico:', m.getNome())
print('Idade objeto m de medico:', m.idade)
print('Numero da Ordem objeto m de medico:', m.numOrdem)






