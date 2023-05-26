print("Sequência de Fibonacci")

inicio = int(input("Quantos termos você quer mostrar? "))

t1 = 0
t2 = 1
i = 3 # começa em 3 pois ja é terceiro termo

print(f"{t1} -> {t2} ", end="")
while i <= inicio:
    t3 = t1 + t2
    print(f"-> {t3} ", end="")
    t1 = t2
    t2 = t3
    i += 1

print("-> Fim!!")