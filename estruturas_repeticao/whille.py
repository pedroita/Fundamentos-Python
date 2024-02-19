numero_escolhido = 9
entrada = int(input("digite um numero  entre 0 e 10: "))

while entrada!= numero_escolhido:
    print("Voce erro, digite novamente")
    entrada = int(input("digite um numero  entre 0 e 10: "))

    
print("Voce acertou!")

cont = 0

while cont <10:
    print (cont)
    cont= cont + 1



for i  in range(1,50,9):
    print (i)

soma = 0

for i in range (1,4):
    notas= float(input(f"Digte sua nota {i}: "))
    soma = soma + notas


print(soma/3)