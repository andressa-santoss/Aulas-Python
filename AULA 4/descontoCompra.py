# Exercicio -- Calculo de desconto em compra


def calcular_valor_compra_com_desconto(valor_compra):

    
    if valor_compra > 200:
        desconto = 0.20  # 20% de desconto
        valor_final = valor_compra * (1 - desconto)
        print(f"Valor da compra com desconto: R$ {valor_final:.2f}")
    else:
        print(f"Valor da compra: R$ {valor_compra:.2f}")



valor = float(input("Digite o valor da compra: R$ "))
calcular_valor_compra_com_desconto(valor)