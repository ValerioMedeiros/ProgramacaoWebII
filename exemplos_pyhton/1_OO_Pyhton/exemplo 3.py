class ObjetoGrafico(object):
    def __init__(self, centro):
        super(ObjetoGrafico, self).__init__()
        self._centro = centro

    @abstractmethod
    def desenha(self):
        pass

    def apaga(self):
        self.setPenColor(self.BACKGROUND_COLOR)
        self.desenha()
        self.setPenColor(self.FOREGROUND_COLOR)

    def movePara(self, p):
        self.apaga()
        self._centro = p
        self.desenho()
