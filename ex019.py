from random import choice
lista = []
for c in range(4):
    aluno = input("Digite o nome do aluno: ")
    lista.append(aluno)

escolhido = choice(lista)
print(f"O aluno sorteado foi {escolhido}")
