# Exercicio - Calcular area e perimetro do retangulo


lado_1 = float(input("Digite o primeiro valor do retângulo: "))
lado_2 = float(input("Digite o segundo valor do retângulo: "))


# calculo perimetro: soma dos lados do retangulo multiplicando por 2
perimetro = (lado_1+lado_2) * 2

# calculo área: multiplicação dos lados
area = lado_1*lado_2

print("O perimentro do retângulo é igual a: ", perimetro)
print("A área do retângulo é igual a: ", area)