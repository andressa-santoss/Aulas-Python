# Exercicio --> Total de contas com o salario


conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))
conta3 = float(input("Digite o valor da terceira conta: "))
salario = float(input("Digite o valor do seu salário: "))


total_contas = conta1 + conta2 + conta3


if salario >= total_contas:
    saldo_restante = salario - total_contas
    print(f"Após pagar as contas, sobrará R$ {saldo_restante:.2f} do seu salário.")
else:
    print("Salário insuficiente!")
