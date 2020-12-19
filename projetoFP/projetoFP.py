#TAD Posicao
#Lista com [a,d]

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
    return isinstance(p, list) and len(p) == 2 and type(p[0]) == type(p[1]) == str and 97 <= ord(p[0]) <= 99 and 3 >= int(p[1]) > 0

def posicoes_iguais(p1, p2):
    return p1 == p2

def posicao_para_str(p):
    return str(obter_pos_c(p) + obter_pos_l(p))

def obter_posicoes_adjacentes(p):
    posicoes = {
        'a1':(['a','2'], ['b', '1'], ['b','2']),
        'a2':(['a','1'], ['a', '3'], ['b','2']),
        'a3':(['a','2'], ['b', '3'], ['b','2']),
        'b1':(['a','1'], ['c', '1'], ['b','2']),
        'b2':(['a','1'], ['a', '2'], ['a','3'], ['b','1'], ['b', '3'], ['c','1'], ['c','2'], ['c', '3']),
        'b3':(['a','3'], ['c', '3'], ['b','2']),
        'c1':(['b','1'], ['c', '2'], ['b','2']),
        'c2':(['c','1'], ['c', '3'], ['b','2']),
        'c3':(['b','3'], ['c', '2'], ['b','2'])
    }
    
    return posicoes[posicao_para_str(p)]

#Fazer TAD peça