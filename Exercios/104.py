def checknumber():
    while True:
        try:
            valor1= int(input("Digite um valor: "))
            if valor1<=0:
                raise ValueError("Erro: O valor precisa ser maior que zero!")
        except ValueError:
            print("Erro favor inserir valor inteiro valido")
        else:
            print(f"O valor digitado foi {valor1}")
        

n = checknumber()
print (f'O valor de n é {n}')


def checknumber2():
    
    while True:
        n = int(input("Digite um valor"))
        if n <0 :
            print ("Digie um valor maior 1")