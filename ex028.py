from random import randint
from time import sleep

# sorteio do número feito com a biblioteca random
numeroSorteio = randint(0, 5)

print("Pensei em um número entre 0 e 5\nTente advinhar!!")
numeroUsuario = int(input("Digite um número: "))

print("Processando...")
sleep(3)

if numeroUsuario == numeroSorteio:
    print("\nVocê acertou o número, parabéns!")
else:
    print("\nVocê errou, tente novamente.")

print(f"O número que eu pensei foi {numeroSorteio}")