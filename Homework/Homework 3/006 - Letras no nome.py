###Faça um algorítmo, em linguagem algorítmica,que leia letras até que a letra Z seja digitada, e exiba a quantidade de letras que foram lidas que são iguais as letras do seu primeiro nome.

#Passos:
#1) Pegar o nome #Ignorar letras maíuculas ou minusculas é um plus
#2) Isolar o primeiro nome (Vou fazer com listas)
#3) ter o input de letras
#3.5) Se o input for maior do que 1 caractere, não armazenar (OPCIONAL)
#4) Se a letra estiver no nome, armazenar em uma outra lista
#5) Print quais letras estavam e a quantidade total de letras (Vou usar conjuntos para isso)

#Definir variáveis
#1) Pegar o nome
nome = input("Qual seu nome?").lower #O .lower deixa tudo minúsculo
#2) Isolar o primeiro nome (Vou fazer com listas)
nome = split(nome)[0] #Split divide a string em varias substrings tranformando em uma lista. Vou pegar dessa lista o primeiro elemento
letras = [] #Defini a variável de letras

while True:
    #3) ter o input de letras
    letra = input("Digite uma letra: ").lower #Cada vez a letra vai mudar
    if letra == "z": 
        break
    #3.5) Se o input for maior do que 1 caractere, não armazenar
    if len(letra) > 1: #Não necessário na tarefa de casa, se a pessoa colocar algo maior que 1 caractere não conta
        print("Você precisa colocar apenas UMA letra")
    if letra in nome: #Se tem letra no nome adiciona a lista
        letras.append(letra) #Coloca a letra em uma lista de letras
        
#Nesse ponto tenho uma lista de letras que estavam no nome
print(letras)