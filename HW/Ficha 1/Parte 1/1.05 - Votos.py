Vbrancos = int(input("Quantos votos brancos? "))
Vnulos = int(input("Quantos votos nulos? "))
Vvalidos = int(input("Quantos votos válidos? "))
total = Vbrancos + Vnulos + Vvalidos
print(f"O total de votos foi de {total}")
print(f"O percentual de votos brancos foi de {Vbrancos/total*100:.2f}%")
print(f"O percentual de votos nulos foi de {Vnulos/total*100:.2f}%")
print(f"O percentual de votos válidos foi de {Vvalidos/total*100:.2f}%")