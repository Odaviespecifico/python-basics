#Como ficaria o algoritmo para calcular a média dos 50 alunos com teste no final usando o comando do-while?

#OBS: Todos os for loop foram modificados para ser while True

#passos
#1) Ler as notas (Pode ser com input ou de um arquivo)
#2) Loop que vai somar todos os números da lista
#3) Dividir a soma pelo tamanho da lista

#1)
notas = [5.95, 9.72, 6.8, 5.4, 6.92, 6.85, 9.97, 6.42, 9.51, 7.9, 1.86, 8.9, 8.31, 9.47, 5.51, 3.87, 6.99, 4.35, 5.52, 1.58, 6.43, 7.21, 1.65, 6.43, 9.18, 6.75, 2.59, 9.08, 1.94, 3.7, 5.08, 8.27, 7.3, 5.06, 6.41, 8.23, 6.47, 9.93, 7.04, 9.51, 5.94, 8.16, 3.72, 1.2, 8.36, 9.75, 7.3, 8.22, 2.96, 4.36, 7.33]
soma = 0

#2) Loop que vai somar todos os números da lista
contador = 0
while True:
    if contador >= 49: #Lembrando que começa em 0
        break
    soma += float(notas[contador]) 
    contador += 1

#3) Dividir a soma pelo tamanho da lista
média = soma/len(notas)

print(f'A média de notas dos alunos é de {média:.2f}')