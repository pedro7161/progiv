
import math as M


class empregado(object):

    def __init__(self, numero=0, nome='', sb=0):
        self.numero = numero
        self.nome = nome
        self.sb = sb
        self.tax = self.calctax()
        self.irs = self.calcirs()
        self.ss = self.calcSS()
        self.sl = self.calsalliquid()

    def calctax(self):
        if self.sb >= 2000.00:
            taxa = 0.25
        if self.sb >= 1000.00 and self.sb < 2000.00:
            taxa = 0.20
        if self.sb < 1000.00:
            taxa = 0.175
        return taxa

    def calcirs(self):
        return self.sb*self.tax

    def calcSS(self):

        return (self.sb-self.irs)*0.11

    def calsalliquid(self):
        return (self.sb-self.irs)-self.ss


class professor(empregado):
    def __init__(self, areaensino=[], numero=0, nome='', sb=0):
        empregado.__init__(self, numero, nome, sb)
        self.areaensino = areaensino


class calculadora():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mult(self):
        return self.x*self.y

    def div(self):
        if(self.x == 0 or self.y == 0):
            return "nao pode ter valores a 0 na divsao"
        else:
            return self.x/self.y

    def som(self):
        return self.x+self.y

    def sub(self):
        return self.x-self.y

    def square(self):
        print("square of first number: ", M.sqrt(self.x),
              "\nsquare of second number:  ", M.sqrt(self.y))

    def loga(self):
        print("log of first number: ", M.log10(self.x),
              "\nlog of second number:  ", M.log10(self.y))

    def sin(self):
        print("sin of first number: ", M.sin(self.x),
              "\nsin of second number:  ", M.sin(self.y))


nome = input("digite o seu nome: ")
numero = input("digite o seu numero: ")
salbruto = float(input("digite o seu salario bruto: "))
emp1 = empregado(numero, nome, salbruto)
print("Salario bruto: ", emp1.sb)
print("SS: ", emp1.ss)
print("IRS: ", emp1.irs)
print("Taxa: ", emp1.tax)
print("Salario liquido: ", emp1.sl)
disciplinas = []
nome = input("digite o seu nome: ")
numero = input("digite o seu numero: ")
ae = input("digite as areas de ensino separadas por virgula: ")
disciplinas = ae.split(",")
salbruto = float(input("digite o seu salario bruto: "))
tea1 = professor(disciplinas, numero, nome, salbruto)
print("Salario bruto: ", tea1.sb)
print("SS: ", tea1.ss)
print("IRS: ", tea1.irs)
print("Taxa: ", tea1.tax)
print("Salario liquido: ", tea1.sl)
print("areas de ensino: ", tea1.areaensino)


n1 = int(input("digite um valor"))
n2 = int(input("digite um valor"))

num = calculadora(n1, n2)
print("divisao: ", num.div())
print("multiplicaçao: ", num.mult())
print("soma: ", num.som())
print("subtraçao: ", num.sub())
num.square()
num.loga()
num.sin()
