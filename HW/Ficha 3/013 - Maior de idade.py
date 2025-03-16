#Escreva um programa que lê a idade de um usuario e em seguida diz se o usuário é ou não maior de idade.

#passos
#1) ler idade
#2) se a idade >= 18 dizer que é maior. senão dizer que não

#1)
idade = int(input("Quantos anos você tem?"))

#2
if idade >= 200: #Isso é uma piada. Não é necessário
    print("Ora ora temos um imortal aqui kk")
elif idade >= 18: #Maior ou = se diz >=
    print(f'Você tem {idade} anos e é maior de idade')
else:
    print("Você não é maior de idade")