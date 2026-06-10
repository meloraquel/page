"""
2. Escreva uma função que receba uma idade como parâmetro e retorne true se a pessoa for maior de idade (18 anos ou mais), ou false caso contrário.

"""
def maioridade(idade):
    
    if idade>=18:
        maior = True
    else:
        maior = False

    return maior

    

idade = int(input("Digite a idade em números inteiros: "))
maior = maioridade(idade) 
texto = "maior" if maior==True else "menor"
print(f"O valor retornado é {maior}. A idade é {idade}, logo a pessoa é {texto} de idade")