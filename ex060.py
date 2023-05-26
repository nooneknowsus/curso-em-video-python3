# from math import factorial
# num = int(input("Digite um número: "))
# print(f"O fatorial de {num} é {factorial(num)}")

numero = int(input("Digite um número para calcular o fatorial: "))
i = numero
# fator nulo multiplicação
fat = 1

while i != 0:

    print(f"{i}", end="")
    print(" x " if i > 1 else " = ", end="")
    fat = fat * i
    i -= 1

print(fat)


# calculo de fatorial com estrutura FOR
# num = int(input("Digite um número: "))
# fat = 1
# for c in range(num, 0, -1):
#       fat*=c
# print(fat)