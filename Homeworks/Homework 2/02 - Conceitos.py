alunos = []
while True:
    try:
        quantidade = int(input('Qual a quantidade de alunos? '))
        break
    except:
        print('Quantidade inválida! tente novamente')

for i in range(quantidade):
    nome = input("Qual o nome do aluno? ")
    media = float(input("Qual a média do aluno? "))
    aluno = {"nome":nome, "Média":media}
    alunos.append(aluno)
i = 0    
for i in range(quantidade):
    if alunos[i]["Média"] <= 4.9:
        conceito = "D"
    elif alunos[i]["Média"] <= 6.9:
        conceito = "C"
    elif alunos[i]["Média"] <= 8.9:
        conceito = "B"   
    else:
        conceito = "A" 
    print(f'{alunos[i]["nome"]} teve nota {alunos[i]["Média"]} e seu conceito foi de {conceito}')