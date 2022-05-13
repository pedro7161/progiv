
def separator(t):
    arr = t.split(" ")
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
    print("unique words: ", uniquelist)
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

    for k, v in positiondic.items():
        for i in v:
            sorted.append(i)

        sorted.sort()

    for number in sorted:
        for k, v in positiondic.items():
            for i in range(len(v)):
                if number == positiondic[k][i]:
                    sentence.append(k)
    return sentence


text = input("digite uma frase: ")
print(separator(text))
