# Faça um algorítmo, em linguagem algorítmica, que leia um número inteiro entre 1 e 8 e 
# exiba o planeta correspondente segundo a tabela abaixo. Utilize a estrutura condicional 
# múltipla(Em linguagem algorítmica: escolha/fimescolha). Caso o usuário informe um 
# número fora do intervalo, exiba a mensagem “Opcao invalida”.

#Passos
#OBS: Tem formas de fazer que não utilizam lista. O progama ficaria com uns 10 if else. Com lista o código fica mais limpo e mais elegante
#1) Definir a lista de planetas
#2) Receber um número do usuário
#3) Se o número for entre 1 e 8 printar formatando o número digitado e o planeta. lembrando que [] depois de uma lista mostra o valor naquela posição da lista. Se não estiver na lista Mostre opção inválida

#1)
planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]

try: #Esse é o método para controlar erros. Não precisa na atividade mas é bom ter e ir se acostumando
    #2)
    num = int(input("Digite um número ")) #Esse tenta rodar 
except ValueError: #Esse é o que fazer se der erro
    print("Você não digitou um número inteiro")
    exit() #Termina o progama
#3)
if num >= 1 and num <= 8:
    print(f"O planeta na posição {num} é {planetas[num-1]}") #O num é -1 pq listas em python começam a contar em 0 e o usuário para pegar o primeiro planeta vai digitar 1
else:
    print("Opção inválida")