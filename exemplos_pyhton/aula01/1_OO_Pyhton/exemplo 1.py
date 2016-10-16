class Complexo(object):
    def __init__(self,real,imaginaria):
        self._real=real
        self._imaginaria=imaginaria
        self.__resultado = real*imaginaria
    def detalhar(self):
        print("Real:",self._real)
        print("Imaginario:",self._imaginaria)
        print("Resultado (privado):",self.__resultado)

    def get_Real(self):
        return self._real
    def set_Real(self,valor):
        self._real=valor
    real=property(fget=get_Real,fset=set_Real)

#Exemplo utilização

c1=Complexo(2,3)
c2=Complexo(1,-5)

print(c1._real)
print(c2._imaginaria)
#print(c2.__resultado)


c1.detalhar()

c2.detalhar()

print("Set real de c1: 10")
c1.real=10
print("Get real de c1:",c1.real)

