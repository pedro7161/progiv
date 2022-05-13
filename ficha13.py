
class empregado(object):

    def __init__(self, numero, nome):
        super(empregado, self).__init__(numero, nome)

    def calctax(salbruto):
        if salbruto >= 2000.00:
            taxa = 0.25
        if salbruto >= 1000.00 and salbruto < 2000.00:
            taxa = 0.20
        if salbruto < 1000.00:
            taxa = 0.175
        print("IRS: ", taxa)
        return taxa

    def calcirs(salbruto):
        taxa = empregado.calctax(salbruto)
        print("salario bruto - irs: ", salbruto-salbruto*taxa)
        empregado.calcSS(salbruto, salbruto*taxa)

    def calcSS(salbruto, irs):

        print("SS: ", (salbruto-irs)*0.11)
        empregado.calsalliquid((salbruto-irs)-(salbruto-irs)*0.11)

    def calsalliquid(salliqu):
        print("salario liquido: ", salliqu)

    class professor():
        def __init__(self, areaensino):
            areaensino = ["ti3", "p3"]


salbruto = float(input("digite o seu salario bruto: "))
empregado.calcirs(salbruto)
print("Salario bruto:", salbruto)
