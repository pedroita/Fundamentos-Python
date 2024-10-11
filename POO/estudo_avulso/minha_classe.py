class ControleRemoto:
    def __init__(self,televisao,comodo):
        self.televisao = televisao
        self.comodo = comodo
    def anvancar_canal(self):
        print('canal Avanco')
    def voltar_canal (self):
        print('Voltando cannal')
    def escolher_canal(self,canal):
        print ('Alterado para o canal : {}' .format(canal))

controle_sala = ControleRemoto('Lg','sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.anvancar_canal()
controle_sala.escolher_canal(25)
controle_sala.voltar_canal()
controle_sala.escolher_canal(10)


# class MinhaClasse:
#     #meu construtor
#     def __init__(self,att):
#         self.meu_atributo = 'Olá Mundo'
#         self.meu_atributo2 = att
#     def meu_metodo(self):
#        print(self.meu_atributo)
#        print(self.meu_atributo2)
#        # print('Estou no metodo!')
    
#     def meu_metodo2(self,num,mult):
#         return num * mult

# objeto =  MinhaClasse('meu atributo 2')
# #print(objeto.meu_atributo2)
# # print(objeto.meu_atributo)
# # objeto.meu_metodo()
# # result = objeto.meu_metodo2(9,5)
# # print(result)
# objeto.meu_metodo()