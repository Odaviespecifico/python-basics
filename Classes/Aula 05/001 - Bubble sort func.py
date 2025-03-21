num = []
while True:
    num.append(float(input("Digite seus números: ")))
    if num[-1] == 0:
        break

def Bsort(num):
    sorte = False
    while sorte == False:
        for i in range(len(num) - 1):
            if num[i] < num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
        for i in range(len(num) - 1):
            if num[i] < num[i+1]:
                break
        else:
            sorte = True
        # print("loop")
    return num
        
                    
print(Bsort(num))