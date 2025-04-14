#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela: 


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


if 9.0 <= media <= 10.0:
    conceito = 'A'
    situacao = 'APROVADO'
elif 7.5 <= media < 9.0:
    conceito = 'B'
    situacao = 'APROVADO'
elif 6.0 <= media < 7.5:
    conceito = 'C'
    situacao = 'APROVADO'
elif 4.0 <= media < 6.0:
    conceito = 'D'
    situacao = 'REPROVADO'
elif 0 <= media < 4.0:
    conceito = 'E'
    situacao = 'REPROVADO'
else:
    conceito = None
    situacao = 'Notas inválidas'


if conceito:
    print(f"\nMédia: {media:.2f}")
    print(f"Conceito: {conceito}")
    print(f"Situação: {situacao}")
else:
    print("\nErro: média fora do intervalo válido (0 a 10).")

