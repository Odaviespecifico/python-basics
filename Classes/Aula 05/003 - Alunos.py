alunos = []

with open("Alunos.csv",'r') as notas:
    for linha in notas.readlines():
        try:
            print(linha)
            nome, nota = linha.split(";")
            alunos.append([nome,nota])
        except ValueError:
            pass

for x in alunos:
        print(f"O aluno {x[0]} tirou {x[1]}")
        
with open("Alunos.csv","a") as notas:
    nnome = "\n" + input("Digite o nome do novo aluno: ").strip()
    nnota = int(input("Digite a nota do novo aluno: "))
    notas.write(f"{nnome};{nnota}")