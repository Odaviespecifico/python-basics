#Agenda eletrônico
#Ler
#adicionar
#Alterar
#apgar
#Listar os dados da agenda
#Deve contar o nome telefone email dos contatos
i = 0
contatos = []

def titulo(msg):
    print('='*len(msg))
    print(msg)
    print('='*len(msg))

def ler():
    global contatos
    with open(r'C:\Users\Davi\Documents\Progamação\python-basics\Classes\Aula 05\contatos.csv','r',encoding='UTF-8') as agenda: 
        i = 0
        contatos = []
        for linha in agenda.readlines():
            contato = linha.split(";")
            contatos.append(dict({'Nome': contato[0], 'Telefone': contato[1], 'Email': contato[2]})) 
def adicionar():
    titulo("Adicionar contato:")
    nome = input('Digite o nome do contato: ').strip()
    telefone = input('Digite o telefone do contato: ').strip()
    email = input('Digite o email do contato: ').strip()
    ncontato = (f"{nome};{telefone};{email}")
    with open(r'C:\Users\Davi\Documents\Progamação\python-basics\Classes\Aula 05\contatos.csv','a', encoding="UTF=8") as agenda: 
        agenda.write(str("\n" + ncontato))
    listar()
def alterar():
    pass
def apagar():
    pass
def listar():
    global contatos
    ler()
    titulo('Contatos na sua agenda:')
    i = 0
    print(contatos)
    for i in range(len(contatos)):
        print(f"Contato {i+1}:")
        for k,v in contatos[i].items():
            print(f"{k}: {v}")

listar()
adicionar()