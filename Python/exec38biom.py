k = int(input("Argumento:"))
menorNatural = 0

def potencia(k):
    n = 1
    menorNatural = 2**n
    while str(menorNatural)[0] != k:
        potencia(n+1)
    return(n)

potencia(k)