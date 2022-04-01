

def ex1(arr):
    media=0
    count=0
    media2=0
    count2=0
    for valor in arr:
        if valor >=18 and valor <=28:
            media+=valor
            count+=1
        media2+=valor
        count2+=1
    if count>0:
        media=media/count
    if count2>0:
        media2=media2/count2
    return "media total: ",media2,"media entre 18 e 28:", media
def ex2(sb):
#     IRS = 20% se salário bruto >= 1000€.
# 15% se salário bruto >= 600€ e < 1000€.
# 10% se salário bruto < 600€.
# Segurança Social = 11% sobre o salário bruto.
    if sb>=1000:
        sal=sb-sb*0.31
    elif sb>=600 and sb <1000:
        sal=sb-sb*0.26
    else:
        sal=sb-sb*0.21
    return "o seu salario",sal
def ex3(arr):
    x=sorted(arr)
    
    return  "o valor intermedio: ",x[1]
i=0
arr=[]
while i<7:
    n1=int(input("digite um numero: "))
    arr.append(n1)
    i+=1
print(ex1(arr))


n_horas=int(input("horas trabalhadas: "))
num=int(input("qual o n de empregado"))
pago_hora=int(input("quanto por hora "))

# Horas Extras = acima de 35H cada Hora vale 1,5H (incluindo horas trabalhadas durante
# o fim de semana).
if n_horas<35:
    salariobruto=n_horas*pago_hora
else:
    n_horasExtra=n_horas*1.5
    salariobruto=n_horasExtra*pago_hora

print(ex2(salariobruto))
arr2=[]
n1=int(input("digite num: "))
n2=int(input("digite num: "))
n3=int(input("digite num: "))
arr2.append(n1)
arr2.append(n2)
arr2.append(n3)
print(ex3(arr2))