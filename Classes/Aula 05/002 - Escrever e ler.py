with open("nomes.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

with open("nomes.txt", "a") as arquivo:
    for i in range(1,11):
        arquivo.write(f"{i} \n")