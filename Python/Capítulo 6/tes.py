def div_int(n, d):
    cnt = 0
    while n >= d:
        cnt += 1
        n -= d
    # neste momento n é o resto. no P4 talvez
    # seja melhor retorna-lo tambem pela pilha
    # em vez de implementar a função resto
    return cnt

def resto(n, d):
    n -= div_int(n,d)*d
    return n

out=[0,0,0,0,0,0]

n=234110

out[0] = div_int(n, 100000)

n = resto(n, 100000)
out[1] = div_int(n, 10000)

n = resto(n, 10000)
out[2] = div_int(n, 1000)

n = resto(n, 1000)
out[3] = div_int(n, 100)

n = resto(n, 100)
out[4] = div_int(n, 10)

out[5] = resto(n, 10)

print(out)