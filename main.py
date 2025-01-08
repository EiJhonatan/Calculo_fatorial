numero = int(input("Digite o número que se desaja determinar o fatorial:"))

fatorial = 1
for termo in range(1,(numero +1)):
    #fatorial= fatorial*termo
    fatorial *= termo
print("O fatorial de " + str(numero) + "! é: " + str(fatorial))