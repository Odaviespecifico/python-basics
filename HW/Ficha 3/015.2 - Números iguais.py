#apenas exemplo de um código mais escalável
números = []
iguais = []
# while True:
#     num = int(input("Digite um número: "))
#     números.append(num)
#     if input("Deseja continuar? (s/n) ") == "n":
#         print(f'Os números digitados foram: {números}')
#         break
#     print(f'O número {num} foi adicionado com sucesso')

números = [3, 5, 6, 6, 3, 6, 3, 2, 2, 4, 5, 1, 0]
for i in range(len(números)):
    if números.count(números[i]) > 1: #Se a contagem de vezes que o número apareceu for maior que 1 singifica que ele se repete
        iguais.append(números[i]) #Adiciona o número a lista de números iguais
    
print(f'A quantidade de números iguais é {len(iguais)}')