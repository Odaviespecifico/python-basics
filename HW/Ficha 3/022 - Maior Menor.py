# Contrua um algoritimo que leia um conjunto de 20 números inteiros e mostre qual foi o maior e o menor valor fornecido

#Passos:
# 1) Criar uma lista para os números com input do usuário (Com for loop)
# 2) Criar um loop para analizar o maior e menor númerando usando if e uma variavel de maior e outra para menor número
# 3) Mostrar o resultado

#1)
números = [int(input("Digite um número: ")) for i in range(20)] #Usando for loop na lista para deixar o código mais clean

#2) Foram iniciadas com o primeiro número da lista para ambas. 
maior = 0
menor = números[0] #Começou com o primeiro número da lista para não ter problemas com o menor número pois se o 0 fosse colocado aqui ele quase sempre seria o menor
for i in range(20):
    if números[i] > maior:
        maior = números[i]
    if números[i] < menor:
        menor = números[i]

#3)
print(f"O maior número é {maior} e o menor número é {menor}")