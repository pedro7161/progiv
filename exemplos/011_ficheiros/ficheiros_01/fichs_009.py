 
fo = open('info.txt', 'r')

while 1:
	ch = fo.read(1)
	if not ch: break # se já chegou ao fim, sair
	
	print(ch)

fo.close()
