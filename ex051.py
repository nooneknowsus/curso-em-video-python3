print("10 TERMOS DE UMA PA")

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

acumulador = termo

for c in range(10):
    print(f"{acumulador} -> ", end="")
    acumulador += razao

    if c == 9:
        print("Acabou")
