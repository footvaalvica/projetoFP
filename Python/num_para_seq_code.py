"""
Suponha que a operacao in nao existia em Python. 
Escreva a funcao pertence, que recebe como argumentos uma lista e um inteiro e 
devolve True se o inteiro está armazenado na lista, False caso contrário. 
Nao pode usar um ciclo for pois este recorre a operacao in.
"""

def pertence(lista,num):
    i = 0
    while i < len(lista):
        if lista[i] == num:
            return True
        i = i + 1
    return False