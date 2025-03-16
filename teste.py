ordenada = False
numeros = []
# Qnum = int(input("Quantos números você quer adicionar? "))
# for i in range(Qnum):
#     numeros.append(int(input("Digite o número: ")))
numeros = [3,5,6,7,3,4,5,2,1,6,3,7]
Qnum = len(numeros)
while ordenada == False: #Isso é uma forma bem rudimentar do bubble sort
    emordem = numeros
    for i in range(0, len(numeros)+1): #Vai subsittuindo um número de cada vez
        try:
            if numeros[i] < numeros[i+1]:
                temp = numeros[i+1]
                numeros[i+1] = numeros[i]
                numeros[i] = temp
                print(numeros)
        except IndexError:
            print("Iteração finalizada")
            if emordem == numeros: #Verifica se está ordenada. Se o ultimo passo deu o mesmo resultado 2 vezes signfica que está ordenada
                print("Está ordenada")
                print(f"A lista ordenada é {numeros}")
                break
            else:
                print("Não está ordenada")
            break