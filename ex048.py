print("Programa que calcula a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500")

somatorio = 0
contador = 0

for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        somatorio += c
        contador += 1
print(f"\nA soma de todos os {contador} números resultam em {somatorio}")
