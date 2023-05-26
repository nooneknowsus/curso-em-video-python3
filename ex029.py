velocidade = float(input("Digite a velocidade do carro: "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print("\nMultado! Você ultrapassou o limite de velocidade que é 80km/h")
    print(f"Sua multa é de R${multa:.2f}")
else:
    print("\nContinue Dirigindo com segurança!")

print("Tenha um bom dia!")