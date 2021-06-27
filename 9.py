#EJEMPLO 9
def factorial(self):
    n= int(input("ingrese la cantidad de numero: "))
    for i in range(n):
    numero=int(input("ingrese numero: "))
    acu=1
    for num in range(numero,1,-1):
        acu=acu*num
    print("numero={}  factorial={}".format(numero,acu))