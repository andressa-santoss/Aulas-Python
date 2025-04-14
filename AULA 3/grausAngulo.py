#  Faça uma programa em Python que peça do usuário 
# um valor em graus para um ângulo. 
# Converta-o para radianos e, usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.

import math

angulo = float(input("Um valor em graus: "))
radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seno de {angulo}°: {seno:.3f}")
print(f"Conseno de {angulo}°: {cosseno:.3f}")
print(f"Tangente de {angulo}°: {tangente:.3f}")

