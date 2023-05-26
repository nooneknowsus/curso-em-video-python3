numero = int(input("Digite um número inteiro: "))

print('''Escolha uma das bases para conversão
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opcao = int(input("Digite sua opção: "))

if opcao == 1:
    print(f"{numero} convertido para Binário é igual a {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido para Octal é igual a {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} convertido para Hexadecimal é igual a {hex(numero)[2:]}")
else:
    print("Opção inválida, tente novamente")