def junta_ordenados(t1,t2):
    i1 = 0
    i2 = 0
    res = ()
    while i1 < len(t1) and i2 < (lenS2):
        if t1[i1] < t1[i2]:
            res = res + (t1[i1],)
            i1 = i1 + 1
        else:
            res = res + (t2[i2],)
            i2 = i2 + 1
    return res + t1[i1:] + t2[i2:]
            
    