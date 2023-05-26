numero = int(input("Digite um número: "))
resp = str(input("Você quer continuar? [S/N]: ")).strip().upper()

contador = acumulador = 0
contador += 1
acumulador += numero

maior = numero
menor = numero

while resp != "N":

    numero = int(input("Digite um número: "))
    contador += 1
    acumulador += numero

    if numero >= maior:
        maior = numero
    elif numero <= menor:
        menor = numero


    resp = str(input("Você quer continuar? [S/N]: ")).strip().upper()[0]


media = acumulador / contador

print(f"\nVocê digitou {contador} números, a soma entre eles resulta em {acumulador}.")
print(f"A média é {media:.2f}.")
print(f"O maior valor digitado foi {maior} e o menor foi {menor}.")