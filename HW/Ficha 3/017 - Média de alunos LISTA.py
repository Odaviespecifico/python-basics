#Como seria um programa para calcular a média de 50 alunos da uma turma
#OBS: Em um progama real as notas dos alunos provavelmente estariam em um documento de texto ou CSV. Vou fazer uma aplicação em uma lista que recebe o input. Vou fazer também uma lista pre-definida só para acelerar o processo de teste do código. Acrecentei um exemplo que utiliza CSV também

#passos
#1) Ler as notas (Pode ser com input ou de um arquivo)
#2) Loop que vai somar todos os números da lista
#3) Dividir a soma pelo tamanho da lista

#1)
notas = [5.95, 9.72, 6.8, 5.4, 6.92, 6.85, 9.97, 6.42, 9.51, 7.9, 1.86, 8.9, 8.31, 9.47, 5.51, 3.87, 6.99, 4.35, 5.52, 1.58, 6.43, 7.21, 1.65, 6.43, 9.18, 6.75, 2.59, 9.08, 1.94, 3.7, 5.08, 8.27, 7.3, 5.06, 6.41, 8.23, 6.47, 9.93, 7.04, 9.51, 5.94, 8.16, 3.72, 1.2, 8.36, 9.75, 7.3, 8.22, 2.96, 4.36, 7.33]
soma = 0

#Alternativa para o primeiro passo (Essa seria com input do usuário:)
# for i in range(1,51):
#     notas.append(int(input("Digite a nota do aluno {i}"))

#Alternativa para o primeiro passo (Esse seria com utilização de arquivo de CSV) [Para ver a aplicação completa consultar 017 Média de alunos CSV]

#2) Loop que vai somar todos os números da lista
for i in range(1,50):
    soma += float(notas[i]) 

#3) Dividir a soma pelo tamanho da lista
média = soma/len(notas)

print(f'A média de notas dos alunos é de {média:.2f}')