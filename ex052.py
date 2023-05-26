n = int(input("Digite um número: "))

acumulador = 0
print()
for c in range(1, n+1):
    divisao = n % c

    if divisao == 0:
        print("\033[33m", end='')
        acumulador += 1
    else:
        print("\033[31m", end='')
    print(f"{c} ", end='')

print(f"\033[m\nO número {n} foi divisível {acumulador} vezes.")
if acumulador == 2:
    print("O número é primo!")
else:
    print("Por isso não é primo.")
print("\nAmarelo representa os números que dividem o número digitado.")