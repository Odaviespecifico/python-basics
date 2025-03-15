import datetime
from datetime import date

ano = int(input("Em que ano você nasceu? "))
mês = int(input("Em que mês você nasceu? "))
dia = int(input("Em que dia você nasceu? "))

dia_nascimento = [ano, mês, dia]

print(dia_nascimento)
data_hoje = datetime.date(ano, mês, dia)
print(date.today())
tempo_de_vida = date.today()-data_hoje
anosdevida = tempo_de_vida.days//365
print("Você tem", anosdevida, "anos de vida")