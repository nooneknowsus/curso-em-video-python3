from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que você deseja: "))

radianos = radians(angulo)

sen = sin(radianos)
cos = cos(radianos)
tang = tan(radianos)

print(f"\nO ângulo de {angulo} tem o SENO de {sen:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cos:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tang:.2f}")