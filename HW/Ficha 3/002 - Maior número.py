# Faça um algoritmo, em linguagem algorítmica, que lê números inteiros positivos, um de cada vez, até que o número zero seja digitado, e exibe o maior número lido. 

#Os passos para resolver esse problema são
# 1) Ler os números inteiros positivos (Precisamos que isso se repita então vamos usar um while Loop. Dica: Para saber qual tipo de loop é melhor é só você se perguntar "Sei quantas vezes quero que esse código se repita?" Se a resposta for sim, geralmente se precisa de um for loop. Caso não um while serve)
# 1.5) Se o número colocado for o maior até o momento guardar ele numa variável
# 2) detectar no loop se 0 estiver presente (Vamos usar if para fazer isso)
# 3) Depois que o número 0 for apertado mostrar o número na varíavel do maior número

maior = 0 #A variavel do maior número (Se não for definida antes da expressão de comparação da erro. Não podemos definir dentro do loop para poder mudarmos o número)

while True: #Iniciar um loop (Não sabemos quanto acaba)
    num = int(input("Insira o número: ")) # 1) Ler um número inteiro positivo dado pelo usuário
    # 1.5) Se o número colocado for o maior até o momento guardar ele numa variável
    if num > maior: #Se o número for maior que o maior, maior vira o número.
        maior = num
    if num == 0: # 2) detectar no loop se 0 estiver presente (Vamos usar if para fazer isso)
        break
    
# 3) Depois que o número 0 for apertado mostrar o número na varíavel do maior número
print(f'O maior número foi {maior}')


#P.S. Um erro comum nesse progama é você escrever errado e dar erro. é possível corrigir isso no python (Não aprendemos isso ainda mas seria assim o loop.)
# while True:
#     try:
#         num = int(input("Insira o número: ")) 
#         if num > maior: 
#             maior = num
#         if num == 0: 
#             break
#     except:
#         print("Número inválido")