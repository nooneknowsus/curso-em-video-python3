maior = 0
menor = 0
for c in range(5):
    peso = float(input(f"Digite o peso da {c+1} pessoa: "))

    if c == 0: # na primeira leitura digitado, ambos valores serão atribuidos como maior e menor, justamente por ser o primeiro valor lido.
        maior = peso
        menor = peso

    else:
        if peso >= maior:
            maior = peso
        elif peso <= menor:
            menor = peso

print(f"\nO maior peso lido foi: {maior}kg")
print(f"O menor peso lido foi: {menor}kg")

