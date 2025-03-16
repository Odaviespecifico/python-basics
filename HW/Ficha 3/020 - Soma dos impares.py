#Escreva um algoritmo que lê 50 números inteiros e em seguida mostra a soma detodos os ímpares lidos.

#Passos
#1) Criar uma lista para os números (Vou colocar com valores aleatório mas nada impede modificar para ser do usuário
#2) Loop que vai somar todos os números ímpares da lista
#3) Mostrar o resultado

import random #Biblitoca para trabalhar com números aleatórios

#1)
números = [random.randint(1,1000) for i in range(50)] #Lista com 50 números aleatórios #Tem como usar for na mesma linha quando estamos dentro de uma lista
print(números)

# #1 alternativo para ter input do usuário:
# for i in range(50):
#     números.append(int(input("Digite um número")))
#2)
soma = 0
for i in range(50):
    if números[i] % 2 != 0: #Se o número for ímpar
        soma += números[i]
#3)
print(f'A soma dos números ímpares é de {soma}')