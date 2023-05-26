distancia = float(input("Digite a distância da viagem (KM): "))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"\nSua viagem é de {distancia}km!")
    print(f"O preço da passagem é R${preco:.2f}")
else:
    preco = distancia * 0.45
    print(f"\nSua viagem é de {distancia}km!")
    print(f"O preço da passagem é R${preco:.2f}")