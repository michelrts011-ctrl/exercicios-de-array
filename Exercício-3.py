import random
temp = []
tempMedia = 0
maiorTemp = 0
menorTemp= 999

for a in range (121):
    temp.append(random.randint(15,40))

    if temp[a] > maiorTemp:
        maiorTemp = temp[a]
    if temp[a] < menorTemp:
        menorTemp = temp[a]

media = sum(temp) / len(temp)
print (maiorTemp,"°C")
print (menorTemp,"°C")
print (media,"°C")