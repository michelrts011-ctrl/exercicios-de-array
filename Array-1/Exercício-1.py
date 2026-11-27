vendas = []
percentual = []
vendedores = []
comissao = 0
valor_comissao = 0
a_receber = []
total = 0
maior = 0
menor = 999999999
maior_nome = 0
menor_nome = 0
for a in range (3):
    vendedores.append(str(input("Digite o seu nome: ")))
    vendas.append(float(input("Digite o valor total das suas vendas: ")))
    comissao = (float(input("Digite a porcentagem da sua comissão: "))) / 100
    percentual.append(comissao)

for b in range (len(vendedores)):
    valor_comissao = vendas[b] * percentual[b]
    a_receber.append(valor_comissao)
    print("O valor da comissão do(a)", vendedores[b] , "foi", a_receber[b])

for c in range (len(a_receber)):
    
    if a_receber[c] > maior:
        maior = a_receber[c]
        maior_nome = vendedores[c]
    
    if a_receber[c] < menor:
        menor = a_receber[c]
        menor_nome = vendedores[c]

total = sum(vendas)
print ("O total de vendas foi:", total)
print (maior, maior_nome)
print (menor, menor_nome)