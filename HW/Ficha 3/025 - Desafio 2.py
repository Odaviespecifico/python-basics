#Esse veio na minha cabeça. Quero que o progama me mostra o processo. Ele deve mostrar "Calculando fatorial de X" e depois cada multiplicação

#Passos
#1) Pedir o número
#2) Fazer um loop que vá de n até 1 e multiplique o fatorial -> 5*4*3*2*1
#3) Mostrar o resultado

n = int(input("Digite um número: "))
print(f"Calculando fatorial de {n}")
operação = 0
fatorial = 1 #Começou com 1 pois 1 * 1 = 1 se começarmos com 0 da errado
for i in range(n,1,-1) : #Começou com 1 pois 0! = 1
    fatorial *= i
    print(f"{fatorial} * {i-1} = {fatorial*(i-1)}")
    
print(f"O fatorial de {n} é {fatorial}")