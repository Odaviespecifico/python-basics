#Faça um algoritmo, em linguagem algorítmica, que calcule a soma dos números inteiros divisíveis por três no intervalo de 1 até o ano do seu nascimento.

#Passos
#1) pegar o ano de nascimento
#2) Fazer um loop que vá de 1 até o ano de nascimento (For loop)
#3) Se o número for divisível por 3, somar a uma variável (Deve ser criada)
#4) Mostrar o resultado

soma = int()
ano = int(input("Em que ano você nasceu? "))

for i in range(3,ano+1):
    if i % 3: #Se o número for divisível por 3
        soma += i #Soma recebe ela mesma + i

if soma == 0: #Não necessário. Se a soma for 0 signfica que nenhum número divisível por 3 foi presente. Isso só se aplica para quem nasceu no ano 1 e 2
    soma = "Nenhum número divisível por 3 encontrado"

#4) Mostrar o resultado
print(soma)