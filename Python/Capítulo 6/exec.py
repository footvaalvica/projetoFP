def cria_rac(n ,d):
    if type(n) == type(d) == int and d > 0:
        return {'n': n, 'd': d}
    else:
        raise ValueError('cria_rac: args invalidos')

def num(r):
    return r['n']

def den(r):
    return r['d']

def eh_racional(arg):
    return isinstance(arg, dict) and len(arg) == 2 and 'd' in arg and 'n' in arg and type(arg['d']) == type(arg['n']) == int and arg['d'] > 0

def eh_rac_zero(r):
    return num(r) == 0

def racionais_iguais(r1, r2):
    return (num(r1) * den(r2)) == (num(r2) * den(r1))

def escreve_rac(r):
    return str(num(r) + '/' + den(r))

def produto_rac(r1, r2):
    return cria_rac(num(r1)*num(r2), den(r1)*den(r2))




#R (n,d) = (n,d)