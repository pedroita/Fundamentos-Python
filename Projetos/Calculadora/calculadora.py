from menu import menu
from funcaosomar import somar
from funcaosubtrair import subtracao
from funcaomultiplicar import multiplicar
from funcaodividir import dividir

@profile
def calcular():
    while True:
        menu()
        try:
            operando = int(input("Qual opção você deseja? "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
            continue

        if operando == 1:
            print (somar())
        elif operando == 2:
            print(subtracao())
        elif operando == 3:
            print(multiplicar())
        elif operando == 4:
            print(dividir())
        elif operando == 0:
            print("Fim da execução")
            break
        else:
            print("OPÇÃO INVÁLIDA")

        if not again():
            print("Muito obrigado, volte mais tarde!")
            break

def again():
    while True:
        calcular_novamente = input("Você deseja calcular novamente? (Digite 'Y' para sim ou 'N' para não): ").upper()
        if calcular_novamente == 'Y':
            return True
        elif calcular_novamente == 'N':
            return False
        else:
            print("Entrada inválida! Tente novamente.")

if __name__ == "__main__":
    calcular()
