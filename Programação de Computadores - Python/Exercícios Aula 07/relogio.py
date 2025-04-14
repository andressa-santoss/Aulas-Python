#Faça um programa em Python que solicite ao usuário uma quantidade de segundos,
#calcule e exiba a quantidade de horas, minutos e segundos.


segundosTotal = int(input("Digite a quantidade de segundos: "))

horas = segundosTotal //3600
sobra = segundosTotal %3600
minutos = sobra //60
segundos = sobra %60

print(f"{segundosTotal} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos")