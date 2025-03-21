#Agenda eletrônico
#Ler
#adicionar
#Alterar
#apgar
#Listar os dados da agenda
#Deve contar o nome telefone email dos contatos
i = 0
contatos = []
with open('contatos.txt','r') as agenda: 
    for linha in agenda.readlines():
        contatos.append(linha.strip())
        
print(contatos[0])
print(contatos)
def ler():
    pass
def adicionar():
    pass
def alterar():
    pass
def apagar():
    pass
def listar():
    print('Contatos na sua agenda:')
    for i in range(len(contatos)):
        print(f"Contato {i+1}:")
        for k,v in contatos[i].items():
            print(f"{k}: {v}")
        print('\n')
            
listar()