from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"O atleta tem {idade} ano(s).")

if idade <= 9:
    print("Sua categoria é: MIRIM")
elif idade > 9 and idade <= 14:
    print("Sua categoria é: INFANTIL")
elif idade > 14 and idade <= 19:
    print("Sua categoria é: JÚNIOR")
elif idade > 19 and idade <= 25:
    print("Sua categoria é: SÊNIOR")
elif idade > 25:
    print("Sua categoria é: MASTER")
