#Escreva um programa que lê um número e em seguida calcula e imprime seu fatorial.
#Esse é um exercício clássico. Recomendo que tentem sem nem mesmo ver os passos para tentar entender o problema e como resolvê-lo
#Dica: O fatorial de um número é o produto de todos os números até ele

#Passos
#1) Pedir o número
#2) Fazer um loop que vá de n até 1 e multiplique o fatorial -> 5*4*3*2*1
#3) Mostrar o resultado

n = int(input("Digite um número: "))

fatorial = 1 #Começou com 1 pois 1 * 1 = 1 se começarmos com 0 da errado
for i in range(n,1,-1) : #Começou com 1 pois 0! = 1
    fatorial *= i
    
print(f"O fatorial de {n} é {fatorial}")