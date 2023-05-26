import random

vetAlunos = []
for c in range(4):
    alunos = input("Digite o nome do aluno: ")
    vetAlunos.append(alunos)

random.shuffle(vetAlunos)

print(f"A ordem de apresentação será: {vetAlunos}")
