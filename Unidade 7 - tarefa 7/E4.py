"""
4. Escreva uma função que receba como parâmetro um número e retorne o fatorial deste número
"""
def fatorial(numero):
    
    fatorial = 1
    if numero < 0:
        print("O fatorial não está definido para números negativos.")
    elif numero == 0 or numero == 1:
        fatorial = 1
    else:
        for i in range(1, numero + 1):
            fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")

numero = int(input("Digite um número: "))
fatorial(numero)