"""
Escreva uma função que receba um vetor de números e retorne o menor elemento do vetor.
"""
# Utilizando o método de inserir o 0 para encerrar a inserção de números no vetor
def MenorElemento():
    valormenor = float("inf")
    vetor = [] 
    while numero!=0:
        numero = int(input("numero: "))
        vetor.append(numero)
        if numero<valormenor:
                valormenor=numero
        elif numero ==0:
             vetor.append(numero)
             break
             
    return valormenor

valormenor = MenorElemento()

# print("\n","-"*30,"\n")
# print(f"O valor do vetor é: {vetor}")
print("\n","-"*30,"\n")
print(f" O valor menor do vetor é: {valormenor}")
print("\n","-"*30,"\n")
