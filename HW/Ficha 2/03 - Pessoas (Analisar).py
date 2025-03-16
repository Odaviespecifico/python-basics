import csv
def maior():
    with open('pessoas.csv') as pessoas:
        leitor = csv.reader(pessoas,"excel",lineterminator="\n")
        maior = 0
        pessoamaior = ""
        linha = 0
        for row in leitor: #Loop que pega a coluna no csv.reader(row) 
            #print(row[1]) #Diz o valor da altura
            if linha == 0: #ignora o cabeçalho
                linha += 1
                continue
            if int(row[1]) > int(maior): #Se o valor da coluna for maior que a memória, define que a memoria vai ser o valor e que a pessoa vai ser o nome
                maior = row[1]
                pessoamaior = row[0]
                #print(f'O maior até agora é {maior}')
                empate = False
            elif int(row[1]) == int(maior): #Caso de empate de altura
                empate = True
                pessoamaior = f'{row[0]} e {pessoamaior}'
            
        if empate == False: #Caso não tenha empate
            print(f'A pessoa com maior altura é {pessoamaior} com a altura de {maior}cm')
        else: #Caso tenha empate
            print(f'Temos um empate entre {pessoamaior} com uma altura de {maior}cm')
def mediamulher():
    #Variáveis locais necessárias:
    Total_mulheres = 0
    soma = 0
    with open('pessoas.csv') as pessoas:
        leitor = csv.reader(pessoas,"excel",lineterminator="\n")
        for row in leitor: #Verifica todas as linhas do arquivo CSV
            if row[2] == '2': #Se a linha do sexo for feminino
                soma += int(row[1]) #Adiciona o valor da altura a soma
                Total_mulheres += 1 #Adiciona 1 ao total
                
        print(f'A média de altura entre as mulheres é de {soma/Total_mulheres:.2f}cm')             
def mediageral():
    #Variáveis locais necessárias:
    total = 0
    soma = 0
    with open('pessoas.csv') as pessoas:
        leitor = csv.reader(pessoas,"excel",lineterminator="\n")
        for row in leitor:
            if 'Nome' in row: #Para ignorar o cabeçalho. Se a palavra nome estiver na iteração row ignorar
                continue
            soma += int(row[1])
            total += 1
                
        print(f'A média de altura entre todos da turma é de {soma/total:.2f}cm')
        
        
maior()
mediageral()
mediamulher()