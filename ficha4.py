def ex1(str):
    print("Ocorrências da Vogal a: ",str.count("a"))
    print("Ocorrências da Vogal a: ",str.count("e"))
    print("Ocorrências da Vogal a: ",str.count("i"))
    print("Ocorrências da Vogal a: ",str.count("o"))
    print("Ocorrências da Vogal a: ",str.count("u"))

def ex2(str):
    start=str.index("b")
    idx=str.index("a")
    print(start)
    
    print("A) ",str[start:len(str)])
    print("B) ",str[0:start])
    print("C) ",idx)
    print("D) ",str.count("a"))
    print("E) ",len(str))
    print("F) ",str.replace(" ","#"))
    print("G) a palavra tejo esta na posiçao: ",str.find("tejo"))
 



ex1(str=input("digite uma frase: "))
# (index, count, in, seletor [:], len, replace,
str= "a amada lisboa e o rio tejo belo encantam toda a gente"
ex2(str.lower())
