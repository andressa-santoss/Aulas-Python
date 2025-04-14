# Exercicio - Calculo raizes de segundo grau com Bhaskara

import math

# Solicita os valores da equação
ladoA = float(input("Digite o valor do lado a: "))
ladoB = float(input("Digite o valor do lado b: "))
ladoC = float(input("Digite o valor do lado c: "))

# Calcular o valor de Delta
delta = ladoA**2 - 4*ladoA*ladoC

# Verifica se as raízes são reais
if delta >= 0:
    # Calcula as raízes
    x1 = (-ladoB + math.sqrt(delta)) / (2 * ladoA)
    x2 = (-ladoB - math.sqrt(delta)) / (2 * ladoA)
    

    print(f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
else:
    print("A equação não possui raízes reais.")

