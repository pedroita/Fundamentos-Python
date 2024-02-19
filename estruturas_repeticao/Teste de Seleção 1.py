entrada = input()

valores = [int(x)for  x in entrada.split(" ")]
a = valores[0]
b = valores[1]
c = valores[2]
d = valores[3]
valido = b>c 
valido = valido and c>a
valido = valido and c +d >a+b

valido = valido and c>0 and d>0
valido = valido and a%2==0 
if (valido):
    print ("valores aceito")
else:
    print ("valores não são aceitos")