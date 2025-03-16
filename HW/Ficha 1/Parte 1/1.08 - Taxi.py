kmincial = int(input("Quantos km no início? "))
kmfinal = int(input("Quantos km no final? "))
litros = int(input("Quantos litros de combustível? "))
preço = 2.59
valor_recebido = float(input("Qual é o valor recebido por passageiros? "))

print(f"O carro percorreu {kmfinal-kmincial} km")
print(f"O valor total gasto foi R${litros*preço:.2f} em gasolina")
lucro = valor_recebido-(litros*preço)
if lucro > 0:
    print(f"O lucro foi R${lucro:.2f}")
else:
    print(f"O prejuízo foi R${(lucro * -1):.2f}")

