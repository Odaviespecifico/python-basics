salário = (input('Qual é o salário do funcionário? R$'))
salário = str.replace(salário, ',', '.')
salário = float(salário)

Aumento = int(input('Qual é a porcentagem do aumento? '))
Aumento = Aumento/100

print(f'O salário de R${salário:.2f} com {Aumento*100}% de aumento, passa a ser R${salário+(salário*Aumento):.2f}')