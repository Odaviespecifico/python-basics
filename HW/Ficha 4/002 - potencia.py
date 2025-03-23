#Esse é bem direto e simples. Não tem nem muitos passos para dividir
num = int(input("Digite o número desejado: "))
pot = int(input("Em qual potência deseja elevar o número? "))

def elevar(n,p):
    return f"{n} elevado a {p} é igual a {n**p}"

print(elevar(num,pot))