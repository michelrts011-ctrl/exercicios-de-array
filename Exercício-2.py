qtdPar = 0
par = []
qtdImpar = 0
impar = []
num = 0

for a in range (6):
    num = (int(input("Digite um número: ")))
    if num %2 == 0:
        par.append(num)
    else:
        impar.append(num)

print (len(par)) 
print (par)
print (len(impar))
print (impar)