#Escreva um programa em Python que resolva o
#problema: “Um Programador com insônia”,
#representado ao lado. Utilize o comando de
#repetição apropriado para o problema.
#Obs: Exibir no final o número de carneirinhos
#contados.

# carneirinho = 0
# Já dormiu 
# SIM  ---> Carneirinho  = 0 
# NÃO  ---> Carneirinho = +1


carneirinho = 0
resp = 'N'

while resp =="N" :
    
    resp = (input("Já dormiu? ")).upper()
    if resp == "N":
        carneirinho = carneirinho+1

print("O número total de carneirinhos é ", carneirinho)


