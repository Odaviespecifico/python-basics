tempo = int(input("Quantos segundos durou o evento?"))
horas = tempo//3600
minutos = tempo%3600//60
segundos = tempo%3600%60
print(f"O evento durou {horas} horas e {minutos} minutos e {segundos} segundos")
