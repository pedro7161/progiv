try:
	fo = open('texto.txt', 'r')
	str = fo.read()
	print(str)
	fo.close()
  
except:
	print('Problema na abertuta do ficheiro')
