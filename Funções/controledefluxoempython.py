# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:48:25 2020

@author: Pedro Italo
"""
x = 10
print ("par" if x % 2 == 0 else "impar")
n=int(input("Digite um numero"))
i=0
while (i<n):
    print(i)
    i+=1
def calcular():
    print ("____________________________")
    print ("Bem-vindo a sua calculadora")
    print("Aqui esta o menu de opções")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Mutiplicar")
    print("4.Dividir")
    print("0.Sair")
    print ("____________________________")

    operando=int(input("Qual opção voce deseja? "))
    if operando==1:
        A=int(input("Digite um valor: "))
        B=int(input("Digite um outro valor: "))
        print('{} + {}= '.format(A,B)) 
        print(A+B)
    elif operando==2:
        A=int(input("Digite um valor: "))
        B=int(input("Digite um outro valor: "))
        print('{} - {}= '.format(A,B)) 
        print(A-B)
    elif operando==3:
        A=int(input("Digite um valor: "))
        B=int(input("Digite um outro valor: "))
        print('{} * {}= '.format(A,B))
        print (A*B)
    elif operando==4:
        A=int(input("Digite um valor: "))
        B=int(input("Digite um outro valor: "))
        print('{} / {}= '.format(A,B)) 
        print(A/B)
    elif operando==0:
        print("Fim da execução")
    else:
        print("OPCAO INVALIDA")
    again()
def again():
    calcular_novamente=input("Você deseja calcular novamente? se sim Digite y ou N pra nao")
    if calcular_novamente.upper()=='Y':
        calcular()
    elif calcular_novamente.upper()=='N':
        print("Muito obrigado,volte mas tarde")
    else:
        again()
calcular()
        
    