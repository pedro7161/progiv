
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

        else:
            positionsaver(word, pos, positiondic)
        pos = pos+1

    return constructor(positiondic, uniquelist)


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


def constructor(positiondic, uniquelist):
    complete = []
    sorting = []

    for k, v in positiondic.items():
        for position in v:
            sorting.append(position)
            sorting.sort()
            print(sorting)

        for position in range(len(uniquelist)):
            for l in v:
                for j in range(len(sorting)):
                    print(j, sorting[j], position,
                          uniquelist[position], l, v)
                    if position < sorting[j]:
                        complete.append(uniquelist[position])
                    else:
                        complete.append(positiondic[k][j])

    return complete


text = input("digite uma frase: ")
print(separator(text))
