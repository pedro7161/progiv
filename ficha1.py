def ex1():
    print("Viva Turma")
def ex2():
    n1=int(input("digite o n1: "))
    n2=int(input("digite o n2: "))
    return n1+n2
def ex3():
    n1=int(input("digite o n1: "))
    n2=int(input("digite o n2: "))
    if n1==n2:
        print("os numeros sao iguais")
    else:
        print("nao sao iguais tente novamente")
        ex3()
def ex4(n):
    if n>=10:
        print("o numero inserido é maior ou igual a 10")
    else:
        print("o numero inserido é menos que 10")
def ex5(n1,n2):
    return (n1+n2)/2
def ex6(a,b):
    return (a*b)/2
def ex7(C): 
    return C * 1.8 + 32


ex1()
print(ex2())
ex3()
print(ex4(int(input("digite um numero: "))))
i=0

n1=int(input("digite um numero: "))
n2=int(input("digite um numero: "))
print(ex5(n1,n2))

a=int(input("digite um numero: "))
b=int(input("digite um numero: "))
print(ex6(a,b))
c=float(input("digite celcius: "))

print(ex7(c))