def exexibir_mensagem(nome = "Anonimo"):
    print (f"ola mundo! {nome}")
    

exexibir_mensagem()


def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados= "\n".join([f"{chave.title()}:{valor}"for chave,valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("zen of python", "beautiful is better than ugly.",autor ="tim petter", ano=1998)

# def criar_carro(modelo,ano,placa,/,marca,moto,combustivel):
#     print(modelo,ano,placa,marca,moto,combustivel)

# criar_carro("Gol",2025,"abc-5558",marca="Fit",moto="1.0",combustivel="gasolina")

# criar_carro()

# def criar_carro2(*,modelo,ano,placa,marca,moto,combustivel):
#     print(modelo,ano,placa,marca,moto,combustivel)
    

# criar_carro2(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fit",moto="1.0", combustivel="Gasolina"  )

# def criar_carro3(modelo,ano,placa,/,*,marca,moto,combustivel):
#     print(modelo,ano,placa,marca,moto,combustivel)
    
# criar_carro3("Palio",1999,"ABC-1234",marca="Fit",moto="1.0", combustivel="Gasolina"  )


def wold_cup_title(pais,*args):
    print(f"Pais : {pais}")
    for titulos in args:
        print(f"total de titulos :{titulos}")
wold_cup_title('Brasil', '1958', '1962', '1970', '1994', '2002')
wold_cup_title('Italia', '2006')

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

final_price = calculate_price(100.0, tax_percentage=9.4 )
print(final_price)