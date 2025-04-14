#Faça um programa em Python que solicite ao usuário sua altura e sexo, calcule e imprima o seu peso ideal. Utilize a seguinte convenção:

#Para homens: (72.7*h) – 58

# Para mulheres: (62.1*h) – 44.7

altura = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo (F/M): ").upper()


if sexo == 'M':
    pesoIdeal = (72.7 * altura) - 58
elif sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7

print(f"Seu peso ideial é de: {pesoIdeal} Kg")