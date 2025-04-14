compra = float(input("Digite o valor total da compra: "))
parcelas = int(input("Digite a quantidade de parcelas (2, 4, 6 ou 8): "))

taxa_juros = {
    2: 0.03,
    4: 0.07,
    6: 0.09,
    8: 0.12
}

if parcelas in taxa_juros:

    total_juros = compra * (1 + taxa_juros[parcelas])

    valor_parcela = total_juros / parcelas

    print(f"Valor total com juros: R$ {total_juros:.2f}")
    print(f"Valor de cada parcela ({parcelas}x): R$ {valor_parcela:.2f}")
else:
    print("Quantidade de parcelas inválida. Escolha entre 2, 4, 6 ou 8.")
