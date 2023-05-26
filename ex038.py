print("Digite números inteiros para ser feita a comparação\n")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("\nO primeiro número digitado é maior.")
elif numero1 == numero2:
    print("\nOs número digitados são iguais.")
else:
    print("\nO segundo número digitado é maior.")