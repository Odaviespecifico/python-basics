#Passos
#1) Criar função que recebe 2 números,
#2) Verificar se o número 2 é 0
#3) Verificar se o número 1 é divisível pelo número 2, se sim retornar True se não retornar False
#4) No algorítimo principal receber input dos números
#5) Chamar a função
#6) fazer a verificação do resultado

#1)
def divisivel(num1,num2): #Criei uma função chamada divisível que recebe 2 valores
    if num2 == 0: 
        return "err0"
    #3)
    if num1 % num2 == 0: #Se o resto da divisão entre os números for 0...
        return True #Return define o valor da função quando rodado
    else:
        return False
    
#ALGORITMO PRINCIPAL
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num2 == 0:
    print("O segundo número não pode ser 0")
    exit() #Termina o progama. Alternativamente você pode fazer um while loop aqui
#5 e 6)
if divisivel(num1,num2) == True: #Se for divisível #Rodei a função aqui e enviei os 2 números necessários
    print(f"O número {num1} é divisível por {num2}")
else:
    print(f"O número {num1} não é divisível por {num2}")