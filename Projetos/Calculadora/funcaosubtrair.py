def subtracao():
    try:
        A = int(input("Digite um valor: "))
        B = int(input("Digite um outro valor: "))
        sub = A - B
        mensagem = f"A subtração de {A} - {B} = {sub}"
        return mensagem
    except ValueError:
        return "Entrada inválida! Por favor, insira números inteiros."
