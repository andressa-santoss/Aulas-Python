# Exercicio Faça um programa em Python que 
# calcule e mostre o valor do volume do tronco de uma pirâmide, 
# para isso o programa deve solicitar ao usuário os 
# valores da altura do tronco da pirâmide (h), 
# o valor da base menor (Bmenor) 
# e o da base maior (Bmaior) e calcular a seguinte expressão:



alturaT = float(input("Digite a altura do tronco: "))

Bmenor = float(input("Digite o valor da base menor: "))

Bmaior = float(input("Digite o valor da base maior: "))

volume = alturaT/ 3 * (Bmaior**2 + Bmenor + (Bmaior**2 * Bmenor**2)**0.5)

print(f"O volume do tronco da pirâmide é: {volume:.2f}")