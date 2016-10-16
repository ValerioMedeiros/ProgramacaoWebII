class Complexo(object):
    def __init__(self,real,imaginario):
        self._real=real
        self._imaginario=imaginario
    def __add__(self, numero_complexo):
        return Complexo(self._real+numero_complexo._real,self._imaginario+numero_complexo._imaginario)
    def __sub__(self, numero_complexo):
        return Complexo(self._real - numero_complexo._real, self._imaginario - numero_complexo._imaginario)
    def __str__(self):
        representacao=""
        if(self._imaginario>0):
            representacao='{}+{}'
        else:
            representacao='{}{}'
        representacao = representacao.format(self._real, self._imaginario)
        return representacao
c1=Complexo(2,-4)
c2=Complexo(1,5)
c3=c1+c2
print(c3)
print(c1)
print(c2)