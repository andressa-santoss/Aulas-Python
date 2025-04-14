# Exercicio -- Calculo do salário com base nas horas e turno trabalhados

def calcular_salario():

    periodo = input("Digite o turno de trabalho: ").upper()
    horasTrab = float(input("Digite a quantidade de horas trabalhadas: "))

    if periodo == 'N':
        valorHora = 45.00
    else:
        valorHora = 37.50

    salario = horasTrab * valorHora
    print(f"O salário do funcionário é: R$ {salario:.2f}")

calcular_salario()
