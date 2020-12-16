#TAD Posicao
#R (a,d) = (a,d)

def cria_posicao(c,l):
    if type(c) == type(l) == str and 97 <= ord(c) <= 99 and 3 >= int(l) > 0:
        return [c,l]
    else:
        raise ValueError('criaposicao: argumentos invalidos')

def obter_pos_c(p):
    return p[0]

def obter_pos_l(p):
    return p[1]

def cria_copia_posicao(p):
    return cria_posicao(obter_pos_c(p),obter_pos_l(p))

def eh_posicao(p):
    return isinstance(p, tuple) and len(p) == 2 and type(p[0]) == type(p[1]) == str and 97 <= ord(p[0]) <= 99 and 3 >= int(p[1]) > 0

def posicoes_iguais(p1, p2):
    return p1 == p2

def posicao_para_str(p):
    return str(obter_pos_c(p) + obter_pos_l(p))

#definir obter_posicoes_adjacentes