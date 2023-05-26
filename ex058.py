from random import randint
from time import sleep

# Sorteio do número do computador
numero_computador = randint(0, 10)
palpites = 0

print("O computador sorteou um número entre 0 e 10\nTente advinhar qual foi\n")
numero_jogador = int(input("Digite um número: "))
palpites += 1
print("Será que advinhou?")
sleep(2)

while numero_jogador != numero_computador:

    if numero_jogador > numero_computador:
        print("O número sorteado é menor!!")
    else:
        print("O número sorteado é maior!!")


    print("\nVocê não advinhou o número sorteado, tente novamente!!")
    numero_jogador = int(input("Digite um número: "))
    palpites += 1

    if numero_jogador == numero_computador:
        sleep(1)
        print()
        print(f"\nNúmero sorteado pelo computador: {numero_computador}\nNumero digitado pelo jogador: {numero_jogador}")
        print("Você acertou o número digitado pelo computador, parabéns!!!")

print(f"Acertou com {palpites} tentativas. Parabéns!")
