#Eu sei que em tese só precisaria fazer 5 pessoas mas fiquei curioso em salvar os dados usando o python para um arquivo csv então criei esse para fazer a lista de pessoas
import csv
import random
rodar = input("Rodar esse código vai apagar todos os nomes de pessoas na lista de pessoas. Você quer continuar? Y/N: ").upper() #Como o cógido vai necessáriamente apagar tudo melhor ter esse aviso
aleatorio = input("Deseja criar valores aleatórios para a altura e sexo das pessoas? Y/N: ").upper()
if rodar == "N":
    print("Quando quiser reiniciar a lista, só falar!")
    exit()


while True: #Esse loop é para garantir que o número de pessoas está correto
    try:
        num = int(input("Quantas pessoas deseja adicionar na lista?"))
        if num <= 0:
            print("O número precisa ser positivo")
        else:
            break
    except:
        print("O número é inválido")

with open('pessoas.csv',mode="w") as pessoas: #Abre o arquivo como editável
    escrever = csv.writer(pessoas,dialect="excel",lineterminator="\n") #Define o estilo do CSV
    escrever.writerow(['Nome',"Altura","Sexo"]) #Escreve a primeira linha do CSV
    for i in range(num): 
        nome = input(f'Qual o nome da pessoa {i+1}? ').capitalize()
        if aleatorio != "Y":
            altura = input(f'Qual a altura em cm de {nome}? ')
            sexo = int(input(f"Qual o sexo de {nome}? 1 para masculino 2 para feminino: "))
        else:
            altura = random.randint(140,220)
            sexo = random.randint(1,2)
        escrever.writerow([nome,altura,sexo])
