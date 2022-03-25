def loop(i):
    k=0
    while k<i:
        print(k) 
        k+=1
def joinstring():
    str1="ana "
    str2="amiga"
    return str1+str2
def pergsoma():
    x=int(input("digite valor 1:"))
    y=int(input("digite valor 2"))
    return x+y
def double(a):
    return a*a

print(loop(int(input("digite um valor para ciclar"))))
print(joinstring())
print(pergsoma())
print(double(int(input("digite um valor para duplicar"))))

