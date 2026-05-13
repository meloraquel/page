"""Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números primos dessa sequência."""

print("Digite uma sequência de números inteiros. Digite 0 para parar.")

numero = int(input("Digite um número"))

while numero!=0:
    if (numero>1 or numero==2 or numero%2!=0):
         for i in range(2,numero):
            if (numero%i!=0 or numero==2 or numero%2!=0):
                print(numero)            
    
    numero = int(input("Digite um número"))
     
