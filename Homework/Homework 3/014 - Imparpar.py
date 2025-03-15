#Escreva um programa que lê um número inteiro e diz se o número é par ou ímpar.

#passos
#1) Ler o número
#2) dizer se é par ou impar

#1)
num = int(input("Digite um número: "))

#2)
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} não é par')