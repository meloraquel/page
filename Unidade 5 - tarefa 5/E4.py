"""4. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números ímpares dessa sequência."""


print("Digite uma sequência de números inteiros. Digite 0 para parar.")
numero = int(input("Digite um número: "))

while (numero!="0"): 
    if (numero%2!=0):   
        print(f"{numero}")
    numero = int(input("Digite um número: "))


    

