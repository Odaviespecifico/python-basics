#Faça um algorítmo, em linguagem algorítmica(ou um programa em C), que leia um número inteiro e informe:
# - Igual ou diferente da quantidade de filhos
# - igual ou deferente do ano do seu nascimento
# par ou impar
# divisível ou não pelo número de

#Passos
# 1) Input de quantidade de filhos, ano de nascimento, par ou impar, nome
# 2) Input do número
# 3) As condições e os prints
# 3.5) Para esse ultimo temos que pegar o primeiro nome. No 006 fiz utilizando uma lista, nesse vou fazer utilizando so string para demonstrar

#1)
filhos = int(input("Quantos filhos você tem? "))
ano = int(input("Em que ano você nasceu? "))
nome = input("Qual o seu nome? ")
#3.5)
primeiroNome = nome[:nome.find(" ")+1] #Sei que parece mágica oq eu fiz mas não é nada complexo. Eu peguei a string nome e mostro do começo até ela encontrar um espaço (Que representa o primeiro número). O "+1" é pq o range vai até um antes do espaço. Ficou confuso? so ler sobre metódo strings

#2)
num = int(input("Digite um número: "))

#3)
if num == filhos:
    print("O número é igual da quantidade de filhos")
else:
    print("O número é diferente da quantidade de filhos")
if num == ano:
    print("O número é igual ao seu ano de nascimento")
else:
    print("O número é diferente do seu ano de nascimento")

if num % 2 == 0: #Se o resto de 2 é 0
    print("O número é par")
else:
    print("O número é impar")

if num == len(primeiroNome): #Se o número é igual o tamanho do primeiro nome
    print("O número é igual o tamanho do seu primeiro nome, que legal")
else:
    print("O número não é igual ao tamanho do seu primeiro nome, que chato")