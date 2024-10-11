from typing import Type
class Interrutor :
    def __init__(self,comodo: str) :
        self.__comodo = comodo

    def acender (self):
        print ("acendendo {}".format(self.__comodo))
    
    def apagar (self):
        print ("apagando {}".format(self.__comodo))

class Pessoa:
    def acender_luz(self, interruptor: Type[Interrutor]):
        interruptor.acender()
    def apagar_luz(self,interruptor:Type[Interrutor]):
        interruptor.apagar()
    
    def dormir(self):
        print('Foi dormir...')

Italo = Pessoa()

interruptor_quarto= Interrutor('quarto')
interruptor_cozinha= Interrutor('Cozinha')

interruptor_quarto.acender()
Italo.acender_luz(interruptor_cozinha)
Italo.apagar_luz(interruptor_quarto)
Italo.dormir()
