num = input("Escreva um inteiro\n")
soma = 0

try:
    for i in num:
        soma = soma + int(i)
    print(soma)

except:
    print("That is not a whole number, Mr. Retard.")