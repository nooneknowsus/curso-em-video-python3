valor = float(input("Preço das compras: R$"))

print('''
FORMAS DE PAGAMENTO

[1] Pagamento à vista dinheiro
[2] Pagamento à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
   novo_preco = valor - (valor * 10 / 100)
   print("Pagamento à vista em dinheiro/cheque tem 10% de desconto.")
   print(f"Sua compra de R${valor:.2f} com 10% de desconto vai custar R${novo_preco:.2f}")
elif opcao == 2:
    novo_preco = valor - (valor * 5 / 100)
    print("Pagamento á vista no cartão tem 5% de desconto.")
    print(f"Sua compra de R${valor:.2f} com 5% de desconto vai custar R${novo_preco:.2f}")
elif opcao == 3:
    valor_parcelas = valor / 2
    print(f"Compra de R${valor:.2f}")
    print(f"Pagamento em 2x sem juros no cartão, 2x de R${valor_parcelas:.2f}")
elif opcao == 4:
    parcelas = int(input("Digite quantas parcelas: "))
    novo_valor = valor + (valor * 20 / 100)
    valor_parcelas = novo_valor / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de R${valor_parcelas:.2f} com juros de 20%")
    print(f"Sua compra de R${valor:.2f} vai custar R${novo_valor:.2f} no final")
else:
    print("Digite uma opção válida, tente novamente.")