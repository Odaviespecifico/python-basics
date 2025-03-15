while True:
    try:
        saldo = input('Qual o saldo médio da conta? R$')
        saldo = float(saldo.replace(',','.')) #Caso o usuário coloque virgula em vez de ponto
        break
    except:
        print('O valor do Saldo é inválido. Tente novamente')
if saldo < 0:
    print('Valor inválido. O saldo médio não pode ser menor do que 0.')
elif saldo <= 500:
    print(f'Você não se qualifica para o crédito.')
elif saldo <= 1000:
    print(f'Parabéns, você qualifica para nosso mais simples nível de crédito. você pode ter um emprestimo de até R${saldo * 0.2:.2f}')
elif saldo <= 2000:
    print(f'Parabéns, você qualifica para nosso segundo nível de crédito. você pode ter um emprestimo de até R${saldo * 0.3:.2f}')
else:
    print(f'Parabéns, você qualifica para nosso mais alto nível de crédito. você pode ter um emprestimo de até R${saldo * 0.4:.2f}')