Q_fun = int(input("Quantos funcionários analizar? "))
funcionários = []
for i in range(Q_fun):
    Funcionário = {}
    Funcionário["nome"] = input("Qual o nome do funcionário? ")
    Funcionário["horas"] = int(input("Quantas horas o funcionário trabalhou? "))
    Funcionário["dependentes"] = int(input("Qual o número de dependentes do funcionário? "))
    funcionários.append(Funcionário)


for i in range(Q_fun):
    salario = funcionários[i]["horas"]*10 + funcionários[i]["dependentes"] * 40
    descontos = 0.13 * salario
    print(f'{funcionários[i]["nome"]} ganha R${salario:.2f}. Os descontos são R${descontos:.2f}. O salário liquido é de R${salario - descontos:.2f}')
