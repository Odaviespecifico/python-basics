item = []
i = 0
soma = 0.0
while True:
    try:
        Quantidade = int(input("Quantos itens deseja adicionar? "))
        break
    except:
        print("Valor invalido! Digite um número inteiro.")
    

for i in range(Quantidade):
    valor = input(f"Qual o valor do item {i+1}: R$")
    valor = valor.replace(",",".")
    valor = float(valor)
    item.append(valor)
    soma += item[i]

print (f"O valor total é R${soma:.2f}")
i = 0
print("Os valores dos itens são: ")
for i in range(Quantidade):
    print (f"O valor do item {i+1} é R${item[i]:.2f}")