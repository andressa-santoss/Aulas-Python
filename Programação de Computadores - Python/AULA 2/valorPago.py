# Execicio - Valor total da conta com comisssão de 10 por cento

valorConta = float(input("Digite o valor total da conta: "))

# calculo da conta multiplicando com a comissão do garçom de 10% ---> *0.5
garcom = valorConta*0.10

# calculo do valor total 
valorTotal = valorConta+garcom

print("O valor total da conta com a comissão do garçom é de: ", valorTotal)