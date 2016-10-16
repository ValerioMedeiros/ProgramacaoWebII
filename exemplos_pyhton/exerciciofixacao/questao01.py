a=int(input("Digite o Primeiro Número")) #Converte em inteiro, aplicado aos demais tipos da linguagem
b=int(input("Digite o Segundo Número"))

for x in range(a,b):
    if (x%4)==0:
        print(x)