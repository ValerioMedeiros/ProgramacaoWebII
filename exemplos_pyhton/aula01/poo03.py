from math import pi
from abc import ABCMeta,abstractmethod #Pacote para determinar que uma classe é abstrata, caso contrário seria possível instanciar
class Ponto(object): #define um ponto
    def __init__(self,x,y):
        self._x=x
        self._y=y
class FiguraGeometrica(object):
    __metaclass__= ABCMeta #Estabelece a classe abstrata
    def __init__(self,centro):
        self._centro=centro
    @abstractmethod #marca o método calculaArea como abstrato
    def calculaArea(self):
        pass
class Quadrado(FiguraGeometrica): #Classe Quadrado herda de Figura Geometrica
    def __init__(self,centro,lado):
        super(Quadrado,self).__init__(centro)
        self._lado=lado
    def calculaArea(self): #Sobrecarga do método abstrato
        return self._lado*self._lado
class Circulo(FiguraGeometrica):
    def __init__(self,centro,raio):
        super(Circulo,self).__init__(centro)
        self._raio=raio
    def calculaArea(self):
        return pow(self._raio,2)*pi()

q=Quadrado(Ponto(2,3),4)
print(q.calculaArea())