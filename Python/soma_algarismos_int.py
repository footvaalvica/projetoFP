num = int(input("Escreva um número inteiro.\n"))
array = [int(x) for x in str(num)]
array.reverse()
string = ""

for i in array:
    string = string + str(i)
print(string)