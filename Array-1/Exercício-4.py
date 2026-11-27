nomes = [] 

while True:
    print ("========MENU========")
    print (f'[1] Cadastrar nome \n[2] Pesquisar nome \n[3] Listar todos os nomes \n[0] Sair do programa')
    cod = int(input(""))

    if cod == 1:
        nome = str(input("Digite o nome que você quer cadastrar: "))
        nomes.append(nome)
    
    if cod == 2:
        busca = str(input("Digite o nome que deseja pesquisar"))
        if busca == nomes:
            print ("Nome cadastrado")
        else:
            print ("Nome não encontrado")
    
    if cod == 3:
        print (nomes)
    
    if cod == 0:
        print ("Saindo do programa...")
    
    else:
        break