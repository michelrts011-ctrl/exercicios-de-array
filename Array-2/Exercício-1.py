#1- Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. No final, mostre:
#a) Qual é a média da turma
#b) Quantos alunos estão acima da média da turma 
#c) Qual foi a maior nota digitada
#d) Em que posições a maior nota aparece

notas = []

for a in range(10):
    nota = float(input(f"Digite a nota do aluno {a + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acimaMedia = 0
for b in notas:
    if b > media:
        acimaMedia += 1

maiorNota = max(notas)

posicoes = []
for c in range(len(notas)):
    if notas[c] == maiorNota:
        posicoes.append(c + 1)

print("A média da turma foi:", media)
print(acimaMedia, "alunos ficaram acima da média da turma")
print("A maior nota da turma foi:", maiorNota)
print("A maior nota aparece na(s) posição(ões):", posicoes)