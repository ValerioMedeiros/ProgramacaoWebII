"""
primeiro = int(input())
segundo = int(input())

soma = 0
for i in range(primeiro,segundo+1):
    if i % 4 ==0 :
        soma = soma +i
        print("-",i)
    elif i % 2 ==0 :
        soma = soma +i
        print("-",i)

print(soma)
"""
"""
lista = [2,4,1,7,8,-1,9,5]

print( lista[1] + lista[3])
"""

"""

def separa(lista):
    resultado = []
    for i in lista:
        if i[0].upper() == "A" :
            resultado.append(i)
    return resultado

print(separa(["bansbdkja","askjdh","kjhk","Aaskldj","lknklj"])) 
"""

def imprimiData(string):
    dia = string.split("/")[0]
    mes = string.split("/")[1]
    ano = string.split("/")[2]
    if not(int(dia)>0 and int(dia)<=31 and 12>=int(mes)>0 ):
        print("Data invalida")
        return None
    meses = ["Janeiro","Fevereiro", "Março", "Abril","Maio", "Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    mes = meses[int(mes)+1]    
    return(dia+" de "+mes+" de "+ano)

print(imprimiData("09/09/2009"))


