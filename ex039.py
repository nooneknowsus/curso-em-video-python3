import datetime as dt

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = dt.date.today().year

idade = ano_atual - ano_nascimento
foi = idade - 18
falta = 18 - idade

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")

if idade < 18:
    print(f"\nAinda falta(m) {falta} ano(s) para o alistamento.")
    print(f"Seu alistamento será em {ano_atual + falta}.")

elif idade == 18:
    print("\nVocê deve se alistar imediatamente.")

else:
    print(f"\nVocê já deveria ter se alistado {foi} ano(s) atrás.")
    print(f"Seu alistamento foi em {ano_atual - foi}")