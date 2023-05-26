print("Condição de existência do triângulo digite os segmentos para ser feita a análise.")

l1 = float(input("Digite o primeiro segmento: "))
l2 = float(input("Digite o segundo segmneto: "))
l3 = float(input("Digite o terceiro segmento: "))

# análise
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("É possivel formar um triângulo!")
else:
    print("Não é possivel formar um triângulo!")
