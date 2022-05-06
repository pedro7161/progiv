
def separator(t):
    arr = t.split(" ")
    # positionsaver(arr)
    return unique(arr)


def unique(arr):
    pos = 0
    uniquelist = []
    positiondic = {}
    positionuniquedic = {}

    for word in arr:

        if word not in uniquelist:
            uniquelist.append(word)
            positionuniquedic[word] = pos

        positionsaver(word, pos, positiondic)
        pos = pos+1

    return constructor(positiondic)


def positionsaver(word, pos, positiondic):
    arr = []
    if word in positiondic:
        arr = positiondic[word]
        arr.append(pos)
        positiondic[word] = arr

    else:
        arr.append(pos)
        positiondic[word] = arr

    return positiondic


def constructor(positiondic):
    sorted = []
    sentence = []

    for k, v in positiondic.items():  # poque tens isto aqui? para adicionar as posiçoes dos array todos num array e meter sort,
        # a minha ideia é comparar as posiçoes ha posiçao dentro do diçionario com o array de posiçoes e trocar esses numeros iguais pela palavra
        # nao se se é nessesario
        # im dumb é a unica cena que vem ha cabeça
        # substituir os numeros pelas palavras,eu é que buguei agora na substituiçao
        for i in v:
            sorted.append(i)

        sorted.sort()

        """ 
            {
            "ola":[1,2],
            "tudo":[3,4]
            }
        
        sorted=[0,1,2,3,4,5] dont need this o pc sabe contar
        
        para numero in sorted
            se o numero tiver no dicionario[array] 
                trocar o numero pela palvavra associada no dicionario
                
        """

    finalstring = ""
    # EStou a pensar
    # tou atento ha ala

    for k, v in positiondic.items():
        for number in sorted:
            for i in range(len(k)):
                print(positiondic[k][i])
                if number == positiondic[k][i]:
                    sentence.append(positiondic[v])
    # for k, v in positiondic.items():
    #     for position in v:
    #         sorting.append(position)
    #         sorting.sort()
    #         print(sorting)

    #     for position in range(len(uniquelist)):
    #         for l in v:
    #             for j in range(len(sorting)):
    #                 print(j, sorting[j], position,
    #                       uniquelist[position], l, v)
    #                 if position < sorting[j]:
    #                     complete.append(uniquelist[position])
    #                 else:
    #                     complete.append(positiondic[k][j].value)

    return sentence


text = input("digite uma frase: ")
print(separator(text))
