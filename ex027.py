nome = input("Digite seu nome: ").strip()
n = nome.split()

print(f"Seu primeiro nome é: {n[0]}")
print(f"Seu ultimo nome é: {n[len(n)-1]}")
