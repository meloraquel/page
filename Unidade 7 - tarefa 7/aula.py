# def msg():
#     print("oi")
#     print("boa noite")

# # chamada
# msg()
# msg()
# nome = input("digite")
# msg()

# #criação de função
# def calcula_media(): #() sem parâmetro e sem retorno.
#     nota1 = float("digite n1")
#     nota2 = float("digite n2")
#     media = (nota1+nota2)/2
#     if media>=6:
#         print(f"{media} Aprovado")
#     else:
#         print(f"{media} Reprovado")

# nome = input("digite o seu nome")
# print(f"boa noite {nome}")
# calcula_media



def calcula_media(nota1,nota2):
    media = (nota1+nota2)/2
    print(f"{media} ")



calcula_media(nota1 = float(input("digite n1")), nota2 = float(input("digite n2")))