def dataExtenso(data):
    meses={"01":"Janeiro","02":"Fevereiro","03":"Março","04":"Abril","05":"Maio","06":"Junho","07":"Julho",
           "08":"Agosto","09":"Setembro","10":"Outubro","11":"Novembro","12":"Dezembro"}

    dia=data[1:2]
    mes=meses[data[3:5]]
    ano=data[6:]

    extenso=dia + " de " + mes + " de "+ano
    return extenso

print(dataExtenso(("05/05/2016")))