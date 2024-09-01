
print ("Calculo da idade para candidato a prefeito e eleitores validados da cidade arcoris ")

idade  = int(input("Digite usa idade: "))

if idade >= 18 and idade <= 21:
    print("Você possui idade pra volta mas não pode ser candidato")
elif idade > 21 and idade <= 71 :
    print("Você pode ser candidato ")
elif idade > 71:
    print("Você não pode mas ser canditado")
else:
    print ("Você não possui idade para votar")  