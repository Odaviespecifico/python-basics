#Passos para resolver
#1) Definir as funções que recebem 2 números e retornam a operação
#2) Chamar o input dos números

def soma(n1,n2):
    return n1 + n2 #Return faz a função retornar o valor quando chaamda (é Como se ela recebesse o valor da variável)
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1/n2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(soma(n1,n2))
print(sub(n1,n2))
print(mult(n1,n2))
print(div(n1,n2))
