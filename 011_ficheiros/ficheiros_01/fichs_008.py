# escrevendo num ficheiro a partir de uma determinada posição
 
fo = open('info.txt', 'r+')

fo.seek(12)

fo.write('ZZZZZZZZZZZ')

fo.close() 






