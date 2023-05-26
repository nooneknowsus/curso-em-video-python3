from random import randint

print("JOGO PAR OU ÍMPAR")
vitorias = 0
derrotas = 0


while True:
    numero = int(input("Diga um valor: "))
    escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    sorteio = randint(1, 10)

    somatorio = sorteio + numero

    print(20 * "--")
    if escolha not in "PI":
        print("Opção inválda tente novamente")

    else:
        if escolha == "P" and somatorio % 2 == 0:
            print(f"Você jogou {numero} e o computador {sorteio}. Total {somatorio} DEU PAR!")
            print("Você Ganhou!")
            vitorias += 1
        elif escolha == "P" and somatorio % 2 == 1:
            print(f"Você jogou {numero} e o computador {sorteio}. Total {somatorio} DEU ÍMPAR")
            print("Você Perdeu!")
            break

        elif escolha == "I" and somatorio % 2 == 1:
            print(f"Você jogou {numero} e o computador {sorteio}. Total {somatorio} DEU ÍMPAR")
            print("Você Ganhou!")
            vitorias += 1
        elif escolha == "I" and somatorio % 2 == 0:
            print(f"Você jogou {numero} e o computador {sorteio}. Total {somatorio} DEU PAR!")
            print("Você Perdeu!")
            break
    print(20 * "--")

print("GAME OVER!!")
print(f"Vitorias: {vitorias}")
