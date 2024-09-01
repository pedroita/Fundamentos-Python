def dizer_oi(nome):
    return f" oi {nome}"

def incentivar_aprender(nome):
    return f"oi {nome}, vamos aprender python"

def mesagem_para_Italo(funcao_mensagem):
    return funcao_mensagem ("Italo")

print(mesagem_para_Italo(incentivar_aprender))
print(mesagem_para_Italo(dizer_oi)
)


def pai():
    print("escrevendo a função da pai () Função")
    def filho1():
        print("Imprimindo filho1 da função ()")
    def filho2 ():
        print("Imprimindo filho2 da função ()")
    filho1()
    filho2()

pai()


def calcualar (operador):
    def somar(a,b):
        return a+b
    def subratir (a,b):
        return a - b
    if operador == "+":
        return somar
    else:
        return subratir

resultado =  calcualar("")(5,6)
print (resultado)