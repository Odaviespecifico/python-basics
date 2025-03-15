#Consultar excercício 2
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