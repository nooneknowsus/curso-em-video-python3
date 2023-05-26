print("Gerador de PA (Progressão Aritmética)\n")

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
pa = termo
i = 1

while i <= 10:
    print(f"{pa} -> ", end="")
    pa += razao

    if i >= 10:
        print("Fim", end="")
    i += 1
