num = int(input('Qual o número?'))
pares = []
print(f'Os números pares até {num} são: ',end="")
for i in range(1,num+1):
    if i == num and num % 2 == 0:
        if i % 2 == 0:
            print(f'{i}. ')
            pares.append(i)
    elif num % 2 != 0 and i == num-1:
        if i % 2 == 0:
            print(f'{i}. ')
            pares.append(i)
    else:
        if i % 2 == 0:
            print(f'{i}, ',end="")
            pares.append(i)