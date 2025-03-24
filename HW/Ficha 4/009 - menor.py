 #temos 2 jeitos de fazer isso. O jeito que usa apenas código para determinar o maior (Vou utilizar esse primeiro) ou usando a função min(Aí adicionariamos os números em uma lista)


#Jeito mais simples de fazer essa função: (Não é bom pq não escala)
def menor(a,b,c):
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < a and c < b:
        return c
    
def menorloop(a,b,c):
    numeros = [a,b,c]
    menor = float('inf') # Menor é um número infinitamente grande (Para caso o utusário coloque só numeros grandes)
    for i in range(3): #3 pq temos 3 números
        if numeros[i] < menor: #Se números for menor que o menor menor recebe o número
            menor = numeros[i]
    return menor

def menorn(*nums): #Fazendo com o asterisco antes eu consigo dar um número arbritrário de números para a função
    menor = float('inf')
    for i in range(len(nums)):
        if nums[i] < menor:
            menor = nums[i]
    return menor

#Python tem uma função de menor já. Usar ela é redundante nesse contexto mas vamos utilizar só para demonstração:
def menornumero(a,b,c):
    numeros = [a,b,c]
    return min(numeros) #Ela basicamente faz o que a função menorn faz
print(menorloop(8,5,7))
    