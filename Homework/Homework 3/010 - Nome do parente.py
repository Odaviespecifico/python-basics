#Faça um algorítmo, em linguagem algorítmica), que leia o nome completo de uma pessoa(nome e sobrenome) e o sexo(M-Masculino/F-Feminino). Caso a pessoa seja do sexo feminino, informe se o nome lido é o da sua mãe, caso a pessoa seja do sexo masculino, informe se o nome lido é o do seu pai
#OBS: Essa questão foi interpretada como: Dado o nome e sexo coloque "O nome do pai é..." ou "O nome da mãe é..." dependendo do sexo

#Passos
#1) Receber o nome
#2) receber o sexo
#3) Se o sexo for masculino -> COlocar texto do pai, se feminino da mãe

#1)
nome = input("Qual o nome do seu parente? ").title() #Coloca a primeira letra de cada palavra maúscula
#2) 
sexo = input("Qual o sexo do seu parente? M/F ").upper() #Tranforma em maúscula pq o usuário nem sempre vai colocar no case certo

#3)
if sexo == "F":
    print(f'O nome da sua mãe é {nome}')
if sexo == "M":
    print(f'O nome do seu pai é {nome}')
else:
    print("Valor inválido")