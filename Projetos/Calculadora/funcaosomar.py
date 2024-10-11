def somar():
    try:
        A = int(input("Digite o primeiro valor: "))
        B = int(input("Digite o segundo valor: "))
        soma = A + B
        mensagem = f"A soma de {A} + {B} é: {soma}"
        return mensagem
    except ValueError:
        return "Entrada inválida! Por favor, insira números inteiros."
