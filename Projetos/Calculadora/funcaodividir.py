def dividir():
    try:
        A = int(input("Digite um valor: "))
        B = int(input("Digite um outro valor: "))
        if B == 0:
            return "Não é possível dividir valores por zero."
        resultado = A / B
        mensagem = f"{A} / {B} = {resultado}"
        return mensagem
    except ValueError:
        return "Entrada inválida! Por favor, insira números inteiros."
