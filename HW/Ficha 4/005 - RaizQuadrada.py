#1) Receber um número inteiro
#2) Verificar se ele tem raiz quadrada exata (Aqui vou fazer isso com controle de erro do python (Try except))
#3) Retornar o valor

def raizexata():
    num = int(input("Qual o número? "))
    raiz = num ** 0.5 #Eleva o número por meio (Tirar raiz quadrada)
    if int(raiz) == raiz: #Se o número convertido a int for igual o número significa que ele é inteiro (O int remove casas decimais de números com casas decimais)
        print("Tem raiz exata")
        return 1
    else:
        print("Não tem raiz exata")
        return 0

raizexata()