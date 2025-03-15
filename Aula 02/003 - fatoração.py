while True:
    try:
        num = int(input("Digite um número para fatorar? "))
        if num >= 10000:
            print("Número grande demais. Vai demorar kk")
        else:    
            numero = num
            break
    except:
        print('input inválido')
        pass
    
fat = []
while True:
    for i in range(2, num):
        while num // i == num / i:
            fat.append(i)
            num /= i
            print(fat)
    break

print(f'Os fatores de {numero} são: ',end="")
for i in range (len(fat)-1):
    print(f'{fat[i]}, ',end="")
print(f'{fat[i+1]}.')