class Complexo(object):
    def __init__(self,real,imaginaria):
        self.__real=real # __ significa que o atributo é privado
        self.__imaginaria=imaginaria
    def getReal(self):
        return self.__real
    def setReal(self,real):
        self.__real=real
    real=property(fget=getReal,fset=setReal)

    def getImaginaria(self):
        return self.__imaginaria
    def setImaginaria(self,imaginaria):
        self.__imaginaria=imaginaria

    imaginaria=property(fget=getImaginaria,fset=setImaginaria)

#Exemplo utilização
c1=Complexo(2,3)
c2=Complexo(1,-5)
print(c1.real)
print(c1.__real)#Erro em função da visibilidade
print(c2.imaginaria)