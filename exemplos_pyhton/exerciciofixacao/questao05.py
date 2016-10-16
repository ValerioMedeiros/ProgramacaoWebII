def fazPergunta():
    print("Qual o melhor sistema operacional para uso sem servidores\n")
    print("As possíveis respostas são:\n")
    print("1 - Windows Server")
    print("2 - Unix")
    print("3 - Linux")
    print("4 - Netware")
    print("5 - Mac OS")
    print("6 - Outro")
    opcao=int(input("Informe a opção:"))
    return opcao

sistemas=[0,0,0,0,0,0]
nomes=["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]
total=0
opcao=fazPergunta()
while (opcao!=0):
    if (opcao>=1 and opcao<=6):
        sistemas[opcao-1]+=1
        total+=1
    opcao=fazPergunta()
print("{0:30} Votos Percentual".format("Sistema Operacional"))
for x in range(len(sistemas)):
    print("{0:30}{1:2d} {2:.2f}%".format(nomes[x],sistemas[x],(sistemas[x]/total)*100))
    
    
    