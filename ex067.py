from time import sleep

while True:
    n = int(input("Deseja ver a tabuada de qual valor? "))
    print(20 * "--")
    if n < 0:
        break
    for c in range(1, 11, 1):
        print(f"{n} x {c} = {c * n}")
    print(20 * "--")

print("Finalizando o programa.")
sleep(1)
