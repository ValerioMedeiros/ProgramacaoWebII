from django.forms import ModelForm,DateInput
from django.forms.models import inlineformset_factory

from enquetes.models import *

class UnidadeForm(ModelForm):
   class Meta:
       model=Unidade
       fields=('descricao','sigla')
       error_messages={
           'descricao':{'required':'Informe a Descrição'},
           'sigla':{'required':'Informe a Sigla'},
       }