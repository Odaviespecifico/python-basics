#Construa um algoritmo que fica lendo indefinidamente numeros positivos. Caso o numero lido seja igual a 0 o algoritmo pára de ler números e imprime a média dos números pares lidos anteriormente

#Passos
#1) Fazer um loop que fica recebendo números e que para se o número for 0
#2) Dentro desse loop, analizar se o ultimo input for par
#3) Se for par, adicionar a uma variável soma
#4) Criar uma variável contador para contar quantos números pares foram lidos
#5) Mostrar a média dos números pares

#1)
soma = 0
contador = 0
while True:
    n = float(input("Digite um número: "))
    if n == 0:
        break
    #2)
    if n % 2 == 0:
        #3)
        soma += n
        #4)
        contador += 1

#5)
print("A média dos números pares é de", soma/contador)

#Caso você queira tirar o .0 do float você pode usar a formatação :g (Geral). Ele também arrendonda por padrão o número para 4 casas decimais (Deixa bem mais clean) Fica assim:
print(f"A média dos números pares é de {soma/contador:g}")

#Caso você queira um que não arredonde pode usar if e else
if soma/contador.is_integer(): #Função do python para saber se o número é inteiro
    print(f"A média dos números pares é de {soma/contador}")
else:
    print(f"A média dos números pares é de {soma/contador)