from math import sqrt

num1 = int(input("Escreva o 1º número\n"))
num2 = int(input("Escreva o 2º número\n"))
num3 = int(input("Escreva o 3º número\n"))
num4 = int(input("Escreva o 4º número\n"))
num5 = int(input("Escreva o 5º número\n"))

media = (num1 + num2 + num3 + num4 + num5)/5
desvioPadrao = sqrt((1/4)*(((num1 - media) + (num2 - media) + (num3 - media) + (num4 - media) + (num5 - media))**2))

print("A média é", media)
print("Desvio padrão é", desvioPadrao)