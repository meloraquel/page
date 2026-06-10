def exibirmenu():
    print("Menu\n")
    print("1 - 5,00")
    print("2 -  4,50 ")
    print("3 - 3,00")
    print("4 - 5,50")
    print("0 - sair")


def escolhausuario():
    exibirmenu()
    opcao = int(input("digite a opção"))
    while True:
        if opcao>=0 and opcao<=4:
            break
        else:
            print("não tem essa opção, digite novamente")
            exibirmenu()
            opcao = int(input("digite a opção"))
    
    if opcao!=0:
        quantidade = int(input("digie a quantidade"))
        while True:
            if quantidade>0:
                break
            else:
                print("Quantidade inválida. Digite novamente")
                exibirmenu()
                quantidade = int(input("digite a quantidade"))
        return [opcao, quantidade]
    else:
        return 0

# escolhausuario()
       

def pedido():
    while True:
        escolha = escolhausuario()
        if escolha==0:
            print("fechando o pedido")
            break
        else:
            escolhausuario()


        

pedido()


    
