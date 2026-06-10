"""
1. Escreva uma função que receba um vetor de números e retorne o menor elemento do vetor.
"""


def MenorElemento():
    # Passos para inserir dados no vetor
    valormenor = float("inf")
    vetor = []
    print("Insira um número ou 'sair' para encerrar.")
    while True:
            numero = input("Insira um valor: ")
            vetor.append(numero)

            if numero=="sair":
                vetor.pop() #Exclui o valor "sair" para que ele não seja adicionado na lista
                break

            try: #teste para verificar se todos os valores da lista são inteiros
                int(numero)
            except ValueError: #É executado quando o valor não é um número inteiro ou tem o valor "sair"
                print("Valor inválido. Por favor, insira um número ou 'sair' para encerrar.")
                vetor.pop()
                continue
            

    # Transformar o vetor que está em string para inteiro
    vetorinteiro = [int(item) for item in vetor]

    # Procura o menor número no vetor de inteiros
    for numero in vetorinteiro:
        if numero<valormenor:
         valormenor=numero

    return valormenor, vetorinteiro



valormenor, vetorinteiro = MenorElemento()

print("\n","-"*30,"\n")
print(f"O valor do vetor é: {vetorinteiro}")
print("\n","-"*30,"\n")
print(f" O valor menor do vetor é: {valormenor}")
print("\n","-"*30,"\n")