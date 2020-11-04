def repete(tup1, n):
    tup2 = ()
    for i in tup1:
        tup2 = tup2 + (i,) * n
    return tup2