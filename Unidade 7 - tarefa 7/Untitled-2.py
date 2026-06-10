"""
Escreva uma função que receba um vetor de números inteiros e um valor inteiro n, e retorne uma nova lista com os n primeiros valores da lista original.
"""
def lista():
    vetor = []
    valor = int(input("Digite a quantidade de numeros: "))
    print("Insira um número ou 'sair' para encerrar.")
    while True:
        numero = input("Insira um valor: ")
        vetor.append(numero)
        if numero=="sair":
            vetor.pop()
            break
        try:
            int(numero)
        except ValueError:
            print("Valor inválido. Por favor, insira um número ou 'sair' para encerrar.")
            vetor.pop()
            continue
    
    print(vetor)    
    
    vetorinteiro = [int(i) for i in vetor]
    print(vetorinteiro)


    

  
    novalista = []
    for vetorinteiro in range(valor):
        novalista.append(vetorinteiro)

    print(f"{novalista}")    
    # return novalista


# novalista = lista()
# 
lista()