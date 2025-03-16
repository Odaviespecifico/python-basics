preço_mar = float(input("Qual o preço da mercadoria em Março? R$"))
preço_abr = float(input("Qual o preço da mercadoria em Abril? R$"))

print(f"O preço da mercadoria aumentou {((preço_abr-preço_mar)/preço_mar)*100:.2f}%")