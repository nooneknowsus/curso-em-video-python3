p1 = float(input("Digite sua nota da P1: "))
p2 = float(input("Digite sua nota da P2: "))

media = (p1 + p2) / 2

print(f"\nSua média foi {media:.1f}")

if media < 5:
    print("Você está reprovado.")

elif media >= 5 and media < 7:
    print("Você está de recuperação")

elif media >= 7:
    print("Você está aprovado.")