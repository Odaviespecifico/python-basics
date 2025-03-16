#Defina o valor das variáveis X, Y e Z, ao final da execução de cada um dos algoritmos a seguir

#Esse exercício é basicamente traduzir o que tem nas tabelas para python

def algorítimo_1(): #Criei uma função chamada algorítimo 1 (Serve para organizar os códigos melhor):
    #Mostrar que está rodando algorítimo 1 (Fiz de um jeito para ficar mais bonito)
    texto = "O algorítimo 1 está rodando!" 
    print('='*len(texto))
    print(texto)
    print('='*len(texto))
    #Definir variáveis
    a = 3
    b = 5
    c = 2
    
    x = a/c
    y = b+c
    
    print(f'As váriaveis tem os seguintes valores: a = {a}; b = {b}; c = {c}; x = {x}; y = {y}')
    
def algorítimo_2():
    #Feito dessa forma só para deixar mais bonito
    texto = "O algorítimo 2 está rodando!" 
    print('='*len(texto))
    print(texto)
    print('='*len(texto))
    #Definir variáveis
    a = int()
    b = int()
    c = int()
    x = float()
    y = float()
    z = float()
    
    #Fazer os calculos e atribuir valores
    a = 4
    b = 20
    c = a + b
    if a < 10 and b > 2: #Essa expresão é verdadeira então vai executar
        x = b + c
        y = b % a
        z = a + b + c/3
    else: #Essa é falsa então não vai executar
        x = c - b
        y = c % b
        z = b - a + c/3
    print(f'As váriaveis tem os seguintes valores: a = {a}; b = {b}; c = {c}; x = {x}; y = {y}')
#Executo as funções:
algorítimo_1()
algorítimo_2()