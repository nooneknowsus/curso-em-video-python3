from random import choice
from time import sleep

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')

opcao = int(input("Qual é sua jogada: "))
computador = ["Pedra", "Papel", "Tesoura"]
jogada_pc = choice(computador)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print()
if opcao == 0 and jogada_pc == "Tesoura": # 0 - pedra
    print(f"Computador jogou {jogada_pc}\nJogador jogou Pedra")
    print("Jogador vence")

elif opcao == 0 and jogada_pc == "Papel":
    print(f"Computador jogou {jogada_pc}\nJogador jogou Pedra")
    print("Computador vence")

elif opcao == 0 and jogada_pc == "Pedra":
    print(f"Computador jogou {jogada_pc}\nJogador jogou Pedra")
    print("Empate")

elif opcao == 1 and jogada_pc == "Pedra": # 1 - papel
    print(f"Computador jogou {jogada_pc}\nJogador jogou Papel")
    print("Jogador Vence")

elif opcao == 1 and jogada_pc == "Tesoura":
    print(f"Computador jogou {jogada_pc}\nJogador jogou Papel")
    print("Computador Vence")

elif opcao == 1 and jogada_pc == "Papel":
    print(f"Computador jogou {jogada_pc}\nJogador jogou Papel")
    print("Empate")

elif opcao == 2 and jogada_pc == "Pedra": # 2 - tesoura
    print(f"Computador jogou {jogada_pc}\nJogador jogou Tesoura")
    print("Computador vence")

elif opcao == 2 and jogada_pc == "Papel":
    print(f"Computador jogou {jogada_pc}\nJogador jogou Tesoura")
    print("Jogador vence")
elif opcao == 2 and jogada_pc == "Tesoura":
    print(f"Computador jogou {jogada_pc}\nJogador jogou Tesoura")
    print("Empate")
else:
    print("Opção inválda! Tente novamente.")