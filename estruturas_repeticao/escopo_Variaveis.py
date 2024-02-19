#escopo local




var_global = "Agilistas"

def escreve_texto():
    var_local = "Pedro Italo"
    print ("varialve local: " + var_local)
    print ("Variavel global: " + var_global)
escreve_texto()

def dobro(x):
    dobro = 2*x
    print ("Dobro = ",dobro)

dobro(9)    

def soma(x,y):
    soma = x+y
    print("Soma = " ,soma)

soma(8,9)

def calcular (x,y):
    print ("Soma = " , x+y)
    print ("Subtração = " , x-y)
    print ("Divisão = " , x/y)
    print ("Multiplicão = " , x*y)

Valor1=  float(input("Digite um numero : "))
Valor2=  float(input("Digite um numero : "))

calcular(Valor1,Valor2)