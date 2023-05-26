precoProduto = float(input("Digite o preço do produto: R$"))
print("Pagamento = [1- Á VISTA C/ DESCONTO | PARCELADO C/ ACRESCIMO)")

opcao = int(input("Digite a opção desejada: "))
op1 = precoProduto - (precoProduto * 10 / 100)
op2 = precoProduto + (precoProduto * 10 / 100)

if opcao == 1:
    print(f"\nO valor R${precoProduto}\nCom desconto de 10% á vista fica R${op1}")
else:
    print(f"\nO valor R${precoProduto}\nCom acrescimo 10% parcelado fica R${op2}")
