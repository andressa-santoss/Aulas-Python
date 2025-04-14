#  Crie um programa em Python que solicite ao usuário a sua idade expressa em anos, meses e dias (variáveis separadas). 
# Calcule e mostre a idade expressa apenas em dias. 
# Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.


anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))


total = (anos*365) + (meses*30) + dias

print(f"Sua idade em dia é: ", total)