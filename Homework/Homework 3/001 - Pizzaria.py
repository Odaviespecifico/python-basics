# 1)  Em  uma  pizzaria  cada  lata  de  refrigerante  custa  R$2,0,  uma  pizza  pequena  custa R$8,0,  uma  pizza  média  custa  R$12,00  e  uma  pizza  grande  custa R$16,00.  Faça  um algoritmo, em linguagem algorítmica, que calcule e exiba o valor da conta de uma única mesa e, sabendo quantas pessoas estão nesta mesa, exiba quanto cada pessoa deve pagar.  Considere  que  a  conta  vai  ser  dividida  igualmente  entre  as  pessoas  da  mesa. Considere que será informado o consumo de refrigerante em lata, pizza pequena, média e grande da mesa.  Não se esqueça de cobrar os 10% do garçom.

#Passos para realizar esse progama (Tentem fazer isso antes de ver a solução):
#1) Definir no python os preços de cada coisa
#2) Receber do usuário: Consumo de refrigerante, pizza pequena, média e grande assim como o número de pessoas.
#3) Pegar os números recebidos do usuário de cada item e multiplicar pelo preço. Depois disso somar esse preço para descobrir o preço total
#4) Adicionar ao total 10% do garçom
#5) Mostrar o preço final e o preço por cada pessoa (Preço final / num pessoas)

#Existe várias formas de resolver esse problema. Vou fazer da que considero mais simples 

#1) Definir no python os preços de cada coisa
P_lata = 2
P_pizza_p = 8
P_pizza_m = 12
P_pizza_G = 16

#2) Receber do usuário: Consumo de refrigerante, pizza pequena, média e grande assim como o número de pessoas.
C_lata = int(input("Quantas latas foram consumidas? "))
C_pizza_p = int(input("Quantas pizzas pequenas foram consumidas? "))
C_pizza_m = int(input("Quantas pizzas médias forma consumidas? "))
C_pizza_g = int(input("Quantas pizzas grandes foram consumidas? "))
num_pessoas = int(input("Quantas pessoas estão na mesa? "))

#3) Pegar os números recebidos do usuário de cada item e multiplicar pelo preço. Depois disso somar esse preço para descobrir o preço total
P_final = P_lata*C_lata + P_pizza_p*C_pizza_p + P_pizza_m*C_pizza_m + P_pizza_m*C_pizza_m #Aqui eu fiz em uma única linha. Se você preferir da pra fazer separado

#4) Adicionar ao total 10% do garçom
P_final *= 1.1

#5) Mostrar o preço final e o preço por cada pessoa (Preço final / num pessoas)
print(f'O valor total foi de R${P_final:.2f}. Como temos {num_pessoas} pessoas na mesa o valor para cada pessoa é de R${P_final/num_pessoas:.2f}') #Uma f string. O ":.2f" faz com que aparecam apenas 2 casa decimais

#Fim
