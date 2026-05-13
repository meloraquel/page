"""1. Escreva um programa que imprima a tabuada de um número inteiro informado pelo usuário."""

tabuada = int(input(f"Digite um número inteiro e será exibido a sua tabuada do 0 até o 10:\n"))

print(f"Tabuada do {tabuada}")

for numero in range(11):
    resultado = tabuada*numero
    print(f"{tabuada} * {numero} = {resultado}")