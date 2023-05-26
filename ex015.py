kmRodado = float(input("Digite a quantidade de Km percorridos: "))
diasAlugados = int(input("Dias de aluguel do carro: "))

aluguel = (diasAlugados * 60) + (kmRodado * 0.15)
print(f"Preço a pagar R${aluguel}")
