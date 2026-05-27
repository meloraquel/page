"""
Escreva um programa que crie um vetor de 10 posições imprima seus valores.
"""
vetor = []

for posicao in range(10):
    valores = int(input("Digite um valor: "))
    vetor.append(valores)

print(vetor)