#Vamos usar datetime para pegar o ano atual; Para ser mais preciso usariamos mes.
import datetime

def idade(nascimento):
    anoatual = datetime.datetime.now().year #Estou associando uma variável ao valor do ano atual
    idade = anoatual - nascimento #A idade é o ano - nascimento
    return idade

print(idade(2005))