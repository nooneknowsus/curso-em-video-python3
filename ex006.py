numero = int(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2) # ou pow(numero, (1/2))

print(f"\nNúmero digitado: {numero}\nO dobro de {numero} vale {dobro}")
print(f"O triplo de {numero} vale {triplo}\nA raiz quadrada de {numero} é igual a {raizQuadrada:.2f}.")
