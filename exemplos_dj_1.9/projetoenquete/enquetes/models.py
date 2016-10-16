from django.db import models

class Questao(models.Model):
    texto_questao=models.CharField("Texto da Questão",max_length=255)
    data_publicacao=models.DateTimeField("Data da Publicação")
    def __str__(self):
        return self.texto_questao
        
class Opcao(models.Model):
    questao=models.ForeignKey(Questao,verbose_name="Questão")
    texto_opcao=models.CharField("Texto",max_length=120)
    votos=models.IntegerField("Número de Votos",default=0)
    def __str__(self):
        return self.questao.texto_questao + "-" + self.texto_opcao
