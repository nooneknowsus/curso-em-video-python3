frase = str(input("Digite uma frase: "))
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("A frase digitada é um palíndromo.")
else:
    print("A frase digitada não é um palíndromo.")
