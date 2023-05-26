soma = 0
cont = 0
cont_par = 0
for c in range(1, 7):
    numero = int(input(f"Digite o {c}° número: "))
    cont += 1
    if numero % 2 == 0:
        soma += numero
        cont_par += 1

print(f"\nVocê informou {cont} números, dos número digitados {cont_par} são pares.")
print(f"A soma dos número pares resulta em {soma}.")