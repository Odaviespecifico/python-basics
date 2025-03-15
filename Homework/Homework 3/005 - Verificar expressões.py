#Essa atividade é mais para você testar seus conhecimentos de expressões. Vou criar uma função que analize a verdade de cada que o usuário colocar

#Criei uma lista com as expressões a serem analizadas. Elas estão como string pq quero mostrar no print a expressão em si e não só o resultado. Para executar uma expressão lógica se ela estiver em string se utiliza o método 
expressões = ["(8+2) == 20 and 15 > 2", "10 < 20 or 5 == 2", "not((10 + 20) == 40)", "20 == 20 and 10 < 8", "not(4 > 5)"]
for i in range(len(expressões)): #Iniciei um for loop que vai até o final da lista de expressões (O len retorna o tamanho da lista)
    print(f'A expressão {expressões[i]} é {eval(expressões[i])}') #usar [i] depois de uma lista retorna o item naquela posição da lista 
print() #Se der print em uma expressão com comparador ela mostra True ou False.


#Se você não entendeu as mudanças feitas da questão para python você pode consultar nesse site "https://pythonacademy.com.br/blog/operadores-aritmeticos-e-logicos-em-python" Ele explica bem direitinho as operações