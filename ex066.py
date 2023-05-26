num = 0
contador = 0
somatorio = 0

while True:
    num = int(input("Digite um valor (999) para parar: "))
    if num == 999:
        break

    contador += 1
    somatorio += num
print(f"A soma dos {contador} valores foi {somatorio}.")