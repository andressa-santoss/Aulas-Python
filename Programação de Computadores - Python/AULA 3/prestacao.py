#  Escreva um programa em Python para calcular o valor de uma prestação em atraso (prestacao). Para isso, obtenha o 
# valor da prestação (valorPrestacao), 
# a porcentagem de multa pelo atraso (multa) e a 
# quantidade de dias de atraso (qtdeDias). 

# Calcular e mostrar o valor da prestação atualizado, sabendo que: 

valor_prestacao = float(input("Digite o valor da sua prestação: "))
multa_atraso = float(input("Digite a porcentagem do seu atraso: "))
dias_atraso = int(input("Digite quantos dias sua prestação está atrasada: "))

prestacao = valor_prestacao+(valor_prestacao*(multa_atraso/100)*dias_atraso)

print(f"O valor da parcela da prestação com atraso em juros: ", prestacao)