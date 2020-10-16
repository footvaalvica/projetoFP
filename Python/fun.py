num = int(input("Escreva um número inteiro.\n"))
array = [int(x) for x in str(num)]
number_so_far = 0

for i in array:
    number_so_far = number_so_far + i

print(number_so_far)