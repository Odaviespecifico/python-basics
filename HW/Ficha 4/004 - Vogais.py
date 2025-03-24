#Basicamente vamos criar uma função que ve se uma letra está dentro de uma lista de vogais (Ignorando se é maiúcula ou minúscula). Se tiver retornar 1. Se não retornar 2
def vogais(letra):
    vogal = ["a","e","i","o","u"]
    if letra.lower() in vogal: #Coloquei o .lower para ignorar se está maisculo ou minusculo
        return 1
    else:
        return 0
    
print(vogais("a"))
print(vogais("A"))
print(vogais("c"))