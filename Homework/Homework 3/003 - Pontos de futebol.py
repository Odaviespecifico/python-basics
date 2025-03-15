# 3)  Faça  um  algoritmo,  em  linguagem  algorítmica,  que  calcule  o  número  de  pontos 
# acumulados por um time de futebol em um campeonato, dada a quantidade de vitórias e a 
# quantidade de empates que o time tem até o momento. Considere que uma vitória vale 3 
# pontos e um empate vale 1 ponto

# Passos para resolver esse problema: (Tentem fazer antes de ver a solução [70% do desafio de progamar é descobrir esses passos])
# 1)  Pegar a quantidade de vitórias e empates que o time tem com input
# 1.5) Calcular o número de pontos (Nesse código vou fazer dentro do print)
# 2) mostrar o número de pontos

# 1)  Pegar a quantidade de vitórias e empates que o time tem com input
vitórias = int(input("Quantas vitórias o time teve? "))
empates = int(input("Quantos empates o time teve? "))
# 1.5) Calcular o número de pontos (Nesse código vou fazer dentro do print)
# 2) mostrar o número de pontos
print(f'O time ganhou {vitórias} vezes e empatou {empates} vezes. Os pontos são {vitórias * 3 + empates}')