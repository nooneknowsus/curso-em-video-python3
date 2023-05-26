altura = float(input("Digite a altura da parede em (m): "))
largura = float(input("Digite a largura da parede em (m): "))

area = altura * largura
pintura = area / 2
print(f"Sua parede tem a dimensão de {altura}x{largura} e sua área é de {area}m²")
print(f"Será necessário {pintura:.2f}l de tinta.")
