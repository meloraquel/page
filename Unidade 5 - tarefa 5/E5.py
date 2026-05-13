"""5. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima a quantidade de números negativos."""

print(f"Programa que recebe uma sequência de números inteiros. Digite 0 para saber a quantidade total de números negtivos digitados na sequência.")
quantidade = 0
numero = int(input("Digige um número:"))

while numero!=0:
    if numero<0:
        quantidade = quantidade +1
    numero = int(input("Digite um número:"))

print(quantidade)
