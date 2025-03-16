#Altere o algoritmo anterior para que ele considere apenas a soma dos ímpares que estejam entre 100 e 200.
#OBS: Unica alteração feita no passo 2 e no range dos números

#Passos
#1) Criar uma lista para os números (Vou colocar com valores aleatório mas nada impede modificar para ser do usuário
#2) Loop que vai somar todos os números ímpares da lista
#3) Mostrar o resultado

import random #Biblitoca para trabalhar com números aleatórios

#1)
números = [random.randint(1,400) for i in range(50)] #Lista com 50 números aleatórios #Tem como usar for na mesma linha quando estamos dentro de uma lista. Para saber mais sobre procure sobre "compreensão de listas em python"
print(números)

# #1 alternativo para ter input do usuário:
# for i in range(50):
#     números.append(int(input("Digite um número")))
#2)
soma = 0
print("Números entre 100 e 200:")
for i in range(50):
    if números[i] % 2 != 0 and 100 >= números[i] <= 100: #Se o número for ímpar
        soma += números[i]
        
        print(números[i], end=' ')
print("") #Para pular uma linha #Embelzamento
#3)
print(f'A soma dos números ímpares entre 100 e 200 é de {soma}')