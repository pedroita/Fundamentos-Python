# atribuição de variaveis
idade = 10
altura = 1.75
numero_complexo = 2+3j
nome = 'italo'
mensagem = 'olá ' + nome + '! Bem-vindo ao Fit'

# Concatenar strings
palavra1 = 'Ola'
palavra2 = ', Mundo'
resultado = palavra1 + palavra2

contPalavra = len(resultado)

acessaPalavra = resultado[0]
pecorrePalavra = resultado[-1]

# manipulação de variaveis
a = 5
b = 57
c = a+b
d = a-b
f = a/b


# boleans
eVerdade = True
efalso = False


# listas
arrayNumber = [1, 2, 3, 4]
arrayName = ['Paulo', 'Maria ', 'Carlos']
arrayMisto = ['dois', 10, True]

# add  na lista
array = [1, 2, 3, 9, 4, 22, 122, 7]
print(array)
array.append(4)
print(array)
array.remove(2)
print(array)
array.sort()
print(array)
# print (idade, altura,numero_complexo,c,d ,f, mensagem, resultado,contPalavra, pecorrePalavra, eVerdade)

# print (arrayMisto,arrayName,arrayNumber)

# tuplas
arrayT1 = (1, 2, 3)
arrayT2 = ('a', 'b', 'c')
arrayT3 = (1, "hello", 3.14)
existe_elemento_1 = 1 in arrayT1
print(existe_elemento_1)

print(arrayT1)
print(arrayT2)
print(arrayT3)

# dicionarios

aluno = {"nome": "Carlos", "idade": 25, "altura": 1.75}

if 'pedro' in aluno:
    print("Nome pertence ao dicioanario")
elif 'idade' in aluno:
    print("NÃO DEU CERTO")
else : print("não deu certo")
