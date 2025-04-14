#Faça um programa em Python que recebe a idade de cada um dos 500 alunos de uma escola, matriculados no Ensino Médio. O algoritmo deverá verificar, calcular e imprimir:

#a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16 anos.
#b) a média da idade dos alunos que não são eleitores.

alunosTotal = 3 #quatidade alterada de 500 para 3
quantVotantes = 0
somaNvotantes = 0
quantNvotantes = 0

for i in range (1, alunosTotal + 1):
    idade = int(input("Digite a sua idade: "))
if idade >=16:
    quantVotantes +=1
else:
    somaNvotantes += idade
    quantNvotantes +=1

if quantNvotantes >0:
    mediaNeleitor = somaNvotantes / quantNvotantes
else:
    mediaNeleitor =0

print(f"a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16 anos são {quantVotantes}")
print(f"b) a média da idade dos alunos que não são eleitores é de: {mediaNeleitor}")