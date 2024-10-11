def multiplicar():
    try:
        A = int(input("Digite um valor: "))
        B = int(input("Digite um outro valor: "))
        resultado = A * B
        mensagem = f"{A} * {B} = {resultado}"
        return mensagem
    except ValueError:
        return "Entrada inválida! Por favor, insira números inteiros."
