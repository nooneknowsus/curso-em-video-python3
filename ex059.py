from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

opcao = 0

while opcao != 5:

    print(f'''\n{25*"-"}
[1] - Somar
[2] - Multiplicar 
[3] - Maior
[4] - Novos números
[5] - Sair do programa
{25*"-"}''')

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print(f"\nA soma dos números digitados: {n1} + {n2} = {n1 + n2}")

    elif opcao == 2:
        print(f"\nA multiplicação dos números digitados: {n1} x {n2} = {n1*n2}")

    elif opcao == 3:
        if n1 == n2:
            print("Os números digitados são iguais!")
        elif n1 >= n2:
            print(f"\nO maior número digitado foi {n1}.")
        elif n1 <= n2:
            print(f"\nO maior número digitado foi {n2}.")

    elif opcao == 4:
        n1 = int(input("\nDigite novamente o primeiro número: "))
        n2 = int(input("Digite novamente o segundo número: "))


sleep(2)
print("Finalizando o programa.")