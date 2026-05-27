"""
Escreva um programa que crie um vetor de 10 posições e informe o índice e o valor do maior e do menor elemento.
"""

vetor = []
valor_maior = 0
indice_maior = 0
valor_menor = float("inf")
indice_menor = float("inf")

for indice in range(3):
    valores = int(input("Digite um valor:"))
    vetor.append(valores)
    if valores> valor_maior:
        valor_maior = valores
        indice_maior = indice
    if valores<valor_menor:
        valor_menor = valores
        indice_menor = indice

print(f"Vetor: {vetor} \n Indice Maior: {indice_maior} \n Valor Maior: {valor_maior} \n Indice Menor: {indice_menor}\n Valor Menor:{valor_menor}")



