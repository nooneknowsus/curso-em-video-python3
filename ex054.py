import datetime as dt

acumulador_maior = 0
acumulador_menor = 0

for c in range(7):
    anoNascimento = int(input(f"Em que ano a {c+1}° pessoa nasceu: "))
    anoAtual = dt.date.today().year
    idade = anoAtual - anoNascimento
    #idade = 2017 - anoNascimento

    if idade >= 18:
        acumulador_maior += 1
    else:
        acumulador_menor += 1


print(f"\nNo total {acumulador_maior} pessoas são maiores de idade.")
print(f"E {acumulador_menor} são menores de idade.")