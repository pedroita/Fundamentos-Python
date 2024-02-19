class Calculadora:
    def calcular (self,op,number1,number2):
        if op == '+':
            return self.__adicionar(number1,number2)
        elif op == '-':
           return self.__subtrair(number1,number2)
        else:
            print('operador invalido')
    def __adicionar(self,number1, number2 ):
        return number1 + number2
    def __subtrair(self,number1, number2 ):
        return number1 - number2
    
calq = Calculadora()

resultado =calq.calcular('+',2,3)
print(resultado)