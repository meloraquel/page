print("=== PROGRAMA PARA ENCONTRAR NÚMEROS PRIMOS ===\n")

entrada = input("Digite uma sequência de números inteiros (separados por espaço): ")

numeros = entrada.split()
indice = 0

print("\nNúmeros primos encontrados:")

while indice < len(numeros):
    numero = int(numeros[indice])
    
    # Verifica se o número é primo
    if numero < 2:
        indice = indice + 1
        continue
    
    eh_primo = True
    divisor = 2
    
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            eh_primo = False
        divisor = divisor + 1
    
    # Se for primo, imprime
    if eh_primo:
        print(numero)
    
    indice = indice + 1
