#Escreva um progama que calcula o produto de dois números lidos sem usar o operador de multiplicaçaõ (*)

#Passos
#1) Pedir os dois números
#2) Fazer um loop que some o primeiro número n vezes onde n é o segundo número
#3) Mostrar o resultado

#1)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

#2)
produto = 0
for i in range(n2):
    produto += n1
    
#3)
print(f'O produto de {n1} e {n2} é {produto}')