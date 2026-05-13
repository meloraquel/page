"""2. Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário."""

numero = int(input("Digite o número para calcular o seu fatorial: \n"))

fatorial = numero

for i in range(numero-1,1,-1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")  