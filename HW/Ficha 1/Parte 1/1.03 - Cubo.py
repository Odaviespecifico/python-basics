while True:
    print("********* Tranformador de cubo 2000 *********")
    num = int(input("Diga um número: "))
    print("O cubo de", num, "é", num**3)
    
    continuar = input("Deseja continuar? (s/n) ")
    if continuar == "n":
        break