def num_para_seq_code(n):
    res = ()
    if isinstance(n, int) and n > 0:
        numero = str(n)
        for i in numero:
            if i == "8":
                newI = 0
                tup = (int(newI), )
                res = res + tup
            elif i == "1":
                newI = 9
                tup = (int(newI), )
                res = res + tup
            elif int(i) % 2 == 0:
                newI = int(i) + 2
                tup = (int(newI), )
                res = res + tup
            else:
                newI = int(i) - 2
                tup = (int(newI), )
                res = res + tup
        return res