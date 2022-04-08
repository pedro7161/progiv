def zoo(name,especie,dic):
    if name !="fim" or especie !="fim":
        dic.update({name:especie})
        return dic
    else:
        return dic

dic={"Ziggy":"canario","Pluto": "cao", "Kitty":"gato", "Nemo": "peixe", "Mickey": "rato"}
name="2"
especie="2"
while(name !="fim" or especie !="fim"):
    print("digite dados de animais, para terminar escreva fim")
    name=input("nome do animal: ")
    print("nota:para terminar digite fim")
    if name=="fim":
        break
    print(name)
    especie=input("especie do animal: ")
    print("nota:para terminar digite fim")
    print(especie)
    print(zoo(name,especie,dic))
print("terminado")

searc=input("procure: ")

for nome,spec in dic.items():
    if nome==searc or spec==searc:
        print(nome,spec)