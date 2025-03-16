ordenada = False
numeros = []
Qnum = int(input("Quantos números você quer adicionar? "))
for i in range(Qnum):
    numeros.append(int(input("Digite o número: ")))

Qnum = len(numeros)
while ordenada == False: #Isso é uma forma bem rudimentar do bubble sort
    emordem = numeros.copy() #Cria uma cópia do número
    for i in range(0, len(numeros)): #Vai subsittuindo um número de cada vez
        try:
            if numeros[i] < numeros[i+1]: #Verifica se o número é menor do que o próximo da lista (Se não for não precisa mudar)
                numeros[i+1],numeros[i] = numeros[i],numeros[i+1] #Inverte os números
                print(numeros)
        except IndexError:
            if emordem == numeros: #Verifica se está ordenada. Se o ultimo passo deu o mesmo resultado 2 vezes signfica que está ordenada
                print(f"A lista ordenada é {numeros}")
                ordenada = True