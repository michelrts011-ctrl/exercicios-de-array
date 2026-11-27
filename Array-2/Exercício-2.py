numI = []
numP = []

while True:
    num = int(input("Digite um número inteiro (número negativo encerra o programa): "))
    if num < 0:
        break
    
    if num % 2 == 0:
        numP.append(num)

    else:
        numI.append(num)

numPa = sorted(numP)
numIm = sorted(numI, reverse=True)

print(numPa)
print(numIm)