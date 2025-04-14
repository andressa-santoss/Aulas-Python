## Escreva um algoritmo que solicite um número ao usuário. 
# 
# Caso seja digitado um valor entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”.





valor = int (input("Digite um valor entre 0 a 9: "))

if 0 <= valor <= 9:
    print("O valor do número está correto!")
else:
    print("Valor esta incorreto :(")
