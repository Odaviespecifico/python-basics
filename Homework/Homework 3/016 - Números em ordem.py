#Escreva um programa que lê três número s inteiros e em seguida imprime os números em ordem crescente
#OBS: O python tem uma função de ordenar listas. Caso você utilizasse ela o código seria bem menos porém como estamos focando em aprender os fundamentos de python vou fazer sem utilizar essa função. Em um exemplo real o ideal seria apenas usar a função. Para isso vamos utilizar um método bem básico de ordenamento de lista. O jeito que esse código foi feito também não é muito eficiente. Se fossemos usar um for loop conseguiriamos fazer ele funcionar de forma mais escalável. Vou demonstrar como isso funcionaria mais abaixo
#Passos:
#01) Pegar os números e colocar em uma lista
#2) Iniciar um loop que verifica se a lista está ordenada. Numa lista ordenada um número vai ser sempre maior que o proximo. 
#3) Verificar se os números estão ordenados. Caso não estejam, alterar a ordem

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o segundo número: "))
numeros = [num1, num2, num3]

while not(num1 >= num2 >= num3): #Enquanto a lista não estiver em ordem
    if num1 <= num2:
        temporário = num1
        num1 = num2
        num2 = temporário
    if num2 <= num3:
        temporário = num2
        num3 = temporário
        num2 = temporário
else: #Usar else depois de while loop mostra uma mensagem ao final do loop
    print(f"Os números ordenados são {num1}, {num2}, {num3}")
    
    
#Se fossemos fazer um algorítimo de ordenar lista fariamos:
#Descobrir se a lista está ordenada
ordenada = False
numeros = []
Qnum = int(input("Quantos números você quer adicionar? "))
for i in range(Qnum):
    numeros.append(int(input("Digite o número: ")))
while ordenada == False: #Isso é uma forma bem rudimentar do bubble sort
    emordem = numeros
    for i in range(1, len(numeros)+1): #Vai subsittuindo um número de cada vez
        try:
            if numeros[i] < numeros[i+1]:
                temp = numeros[i-1]
                numeros[i-1] = numeros[i]
                numeros[i] = temp
        except IndexError:
            print("Lista finalizada")
    if emordem == numeros: #Verifica se está ordenada. Se o ultimo passo deu o mesmo resultado 2 vezes signfica que está ordenada
        print("Está ordenada")
        print(f"A lista ordenada é {numeros}")
        break
    else:
        print("Não está ordenada")
