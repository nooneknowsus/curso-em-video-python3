sexo = ""

sexo = input(("Informe seu sexo [F/M]: ")).upper().strip()[0]

while sexo != "M" and sexo != "F":
    print("\nOpção inválida, tente novamente.")
    sexo = input(("Informe seu sexo [F/M]: ")).upper()

print(f"Sexo {sexo} registrado com sucesso!")