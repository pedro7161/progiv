try:
	fo = open('ABC.txt', 'r')
	str = fo.read()
	print(str)
	fo.close()
  
except:
	print('Problema na abertuta do ficheiro')
