#1) Receber um número fora da função
# 2) Criar função que recebe o número como parâmetro
# 3) O fatorial de um número é o número multiplicado pelo seu antecessor, até chegar a 1

num = int(input("Qual o número que você quer fatorial? "))

def fatorial(num):
    i = 1 #Uma váriavel qualquer recebe o valor de 1 (O neutro da multiplicação)
    for i in range(num - 1,1,-1): #Começamos a contar de um número antes do numero dado até 1
        num *= i #Multiplicamos o número dado por esses números até chegar a 1
    return num #Retornarmos o número

print(fatorial(num))