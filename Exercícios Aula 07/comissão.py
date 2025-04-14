#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um
#programa em Python que receba o salário fixo do funcionário e o valor de suas vendas,
#calcule e mostre a comissão e o salário final do funcionário.




salario = float(input("Digite o salario total do salario do funcionario: "))

funcionario = salario*0.04


valorTotal = funcionario+salario

print(f"O valor da comissão é: {funcionario} %")
print(f"O valor do salario com a comissão do funcionario é de R$ {valorTotal} reais")