 
# classes_001
 
''' 
   Uma classe é um programa referência que funciona como modelo ou template para 
   a criação de programas concretos concebidos assim à sua imagem.

   Como programa referência somente pode tornar-se "realizável" através das suas 
   instâncias, que são como cópias, réplicas concretas, os denominados objectos.

   Ou seja, as classes para poderem ser "utilizadas" devem ser instanciadas, que 
   é um processo que consiste na criação de objectos, os quais são assim réplicas 
   acessíveis e utilizáveis da classe.

   Na sua forma, uma classe é um tipo de dados definido pelo programador, semelhante 
   a uma estrutura, mas com a capacidade de poder conter funções para além dos dados.

   Os dados da classe são conhecidos por atributos, propriedades ou caracetrísticas.

   As funções são conhecidas por métodos da classe. Elas vão agir sobre os dados da classe.	 

   Vejamos um exemplo de uma classe básica:

'''
# definição da classe Pessoa
class Pessoa:
	def __init__(self, nome):
		self.nome = nome

# definição do objeto pess usando o construtor		
pess = Pessoa('lia matos')
print(pess.nome)
 

'''
Notas sobre o código acima:

A cláusula init é conhecida pelo construtor.
O construtor é um método chamado automaticamente no momento da 
instanciação de um objecto.
A sua finalidade é inicializar os data members que desejarmos.

cláusula self refere-se ao objeto corrente

'''
