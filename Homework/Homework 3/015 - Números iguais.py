#Escreva um programa que lê tres numeros e em seguida imprime quantos deles são iguais.

#passos
#1) Ler os números
#2) Verificar quantos são iguais. Existem diversas formas de fazer isso. Vou fazer da forma mais simples que verifica se todos sõo iguais, se dois são iguais ou se nenhum é igual.

#1)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

#2)
if num1 == num2 and num1 == num3:
    print("Os três números são iguais")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Dois números são iguais")
else:
    print("Nenhum número é igual")
    
#OBS: NA maior parte dos códigos o ideal é que você tente fazer um código que é facil de aumentar a escala. Se nesse código eu tivesse que fazer 4 números eu precisaria refazer muito do código. Vou fazer um 015.2 que é escalável para demonstrar essa diferença