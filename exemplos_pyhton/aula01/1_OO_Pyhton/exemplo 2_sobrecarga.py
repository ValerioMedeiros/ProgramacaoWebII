class Complexo(object):
    def __init__(self,real,imaginario):
        self._real=real
        self._imaginario=imaginario
    def __str__(self):
        representacao=""
        if(self._imaginario>0):
            representacao='{}+{}'
        else:
            representacao='{}{}'
            representacao = representacao.format(self._real,self._imaginario)
        return representacao
c1=Complexo(2,-4)
c2=Complexo(1,5)
print(c1)
print(c2)

