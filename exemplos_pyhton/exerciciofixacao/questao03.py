def separa(lista):
    result=[]
    for s in lista:
        if (s[0].upper()=='A'): #Converte para maiúsculo
            result.append(s) #adiciona elemento na lista
    return result

lista=["André","Gustavo","Duarte","Almeida"]
print(separa(lista)) #Imprime a lista completa