preco = float(input("Digite o preço do produto: R$"))
desconto = preco - (preco * 5 / 100)

print(f"O produto custa R${preco}\nDesconto de 5% --> R${desconto:.2f}")
