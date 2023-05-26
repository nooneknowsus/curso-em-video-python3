peso = float(input("Qual é seu peso? (KG) "))
altura = float(input("Digite sua altura? (M) "))

imc = peso / (altura ** 2)
print(f"Seu Índice de Massa Corporal é {imc:.1f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está sobrepeso.")
elif imc >= 30 and imc < 40:
    print("Você está obeso.")
else:
    print("Você está em obesidade mórbida, procure um médico.")
