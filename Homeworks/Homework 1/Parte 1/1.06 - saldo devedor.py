cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'pretoebranco': '\033[7;30m'}

prestações = int(input("Quantas prestações você tem? "))
quantidade = int(input("Quantas prestações você já pagou? "))
valor = float(input("Qual é o valor da prestação? "))

print(f"Como você pagou {cores['verde']}{quantidade}{cores['limpa']} de {cores['roxo']}{prestações}{cores['limpa']} prestações,você ainda deve pagar {cores['vermelho']}{prestações-quantidade}{cores['limpa']} prestações")
print(f"O valor total da dívida é de R${cores['vermelho']}{prestações*valor:.2f}{cores['limpa']}")
print(f"Você já pagou R${quantidade*valor:.2f}")
