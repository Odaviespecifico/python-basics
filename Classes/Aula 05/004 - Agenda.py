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
        agenda.write(str(ncontato))
    listar()

def alterar():
    global contatos
    ler()
    titulo("Alterar contato:")
    num = int(input('Digite o contato que deseja alterar: '))
    contatinho = contatos[num-1]
    print(f"Alterando o contato de {contatinho['Nome']}")
    contatinho["Nome"] = input('Digite o nome do contato: ').strip()
    contatinho["Telefone"] = input('Digite o telefone do contato: ').strip()
    contatinho["Email"] = str(input('Digite o email do contato: ')+"\r")
    with open(r'C:\Users\Davi\Documents\Progamação\python-basics\Classes\Aula 05\contatos.csv','w', encoding="UTF=8") as agenda:
        for linha in range(len(contatos)):
            line = contatos[linha]["Nome"] + ";" + contatos[linha]["Telefone"] + ";" + contatos[linha]["Email"]
            agenda.write(line)
    listar()
     
def apagar():
    global contatos
    num = int(input('Digite o número do contato que deseja apagar: '))
    nome = contatos[num-1]['Nome']
    contatos.pop(num-1)
    with open(r'C:\Users\Davi\Documents\Progamação\python-basics\Classes\Aula 05\contatos.csv','w', encoding="UTF=8") as agenda:
        for linha in range(len(contatos)):
            line = contatos[linha]["Nome"] + ";" + contatos[linha]["Telefone"] + ";" + contatos[linha]["Email"]
            agenda.write(line)
    print(f"Contato de {nome} apagado com sucesso!")
    listar()

def listar():
    global contatos
    ler()
    titulo('Contatos na sua agenda:')
    i = 0
    for i in range(len(contatos)):
        print(f"Contato {i+1}:")
        for k,v in contatos[i].items():
            print(f"{k}: {v}")

while True:
    try:
        titulo("Agenda Eletrônica")
        print("1 - Listar contatos")
        print("2 - Alterar contato")
        print("3 - Apagar contato")
        print("4 - Adicionar contato")
        print("5 - Sair")
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            listar()
        elif op == 2:
            alterar()
        elif op == 3:
            apagar()
        elif op == 4:
            adicionar()
        elif op == 5:
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Opção inválida!")
        