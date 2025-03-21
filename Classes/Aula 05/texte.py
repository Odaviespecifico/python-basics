contatos = {"Nome": "Claúdia", "Telefone":"81 9 9853-4563","Email":"Claúdia.maria@gmail.com"}
with open('contatos.txt','a') as agenda: 
    agenda.write(str(contatos))