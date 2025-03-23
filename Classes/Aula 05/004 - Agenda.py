#Agenda eletrônico
#Ler
#adicionar
#Alterar
#apgar
#Listar os dados da agenda
#Deve contar o nome telefone email dos contatos
i = 0
contatos = []

def ler():
    with open(r'C:\Users\Davi\Documents\Progamação\python-basics\Classes\Aula 05\contatos.txt','r') as agenda: 
        for linha in agenda.readlines():
            contatos.append(eval(linha.strip()))
def adicionar():
    pass
def alterar():
    pass
def apagar():
    pass
def listar():
    print('=======================')
    print('Contatos na sua agenda:')
    print('=======================')
    for i in range(len(contatos)):
        print(f"Contato {i+1}:")
        for k,v in contatos[i].items():
            print(f"{k}: {v}")
        print('\n')
            
listar()