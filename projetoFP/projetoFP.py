#TAD Posicao
#Lista com [a,d]

from functools import reduce

def cria_posicao(c,l):
    if type(c) == type(l) == str and 97 <= ord(c) <= 99 and 3 >= int(l) > 0:
        return [c,l]
    else:
        raise ValueError('cria_posicao: argumentos invalidos')

def obter_pos_c(p):
    return p[0]

def obter_pos_l(p):
    return p[1]

def cria_copia_posicao(p):
    return p

def eh_posicao(p):
    return isinstance(p, list) and len(p) == 2 and type(p[0]) == type(p[1]) == str and 97 <= ord(p[0]) <= 99 and 3 >= int(p[1]) > 0

def posicoes_iguais(p1, p2):
    return p1 == p2 and eh_posicao(p1) and eh_posicao(p2)

def posicao_para_str(p):
    return str(obter_pos_c(p) + obter_pos_l(p))

def obter_posicoes_adjacentes(p):
    posicoes = {
        'a1':(['a','2'], ['b', '1'], ['b','2']),
        'a2':(['a','1'], ['a', '3'], ['b','2']),
        'a3':(['a','2'], ['b', '3'], ['b','2']),
        'b1':(['a','1'], ['c', '1'], ['b','2']),
        'b2':(['a','1'], ['a', '2'], ['a','3'], 
        ['b','1'], ['b', '3'], ['c','1'], ['c','2'], ['c', '3']),
        'b3':(['a','3'], ['c', '3'], ['b','2']),
        'c1':(['b','1'], ['c', '2'], ['b','2']),
        'c2':(['c','1'], ['c', '3'], ['b','2']),
        'c3':(['b','3'], ['c', '2'], ['b','2'])
    }
    
    return posicoes[posicao_para_str(p)]

#TAD peça 
# [1/0/-1]

def cria_peca(j):
    if j == 'X':
        return 1
    elif j == ' ':
        return 0
    elif j == 'O':
        return -1
    else:
        raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
    return j

def eh_peca(j):
    return type(j) == int and -1 <= j <= 1

def pecas_iguais(j1, j2):
    return j1 == j2 and eh_peca(j1) and eh_peca(j2)

def peca_para_str(j):
    if j == 1:
        return '[X]'
    if j == 0:
        return '[ ]'
    if j == -1:
        return '[O]'

def peca_para_inteiro(j):
    return cria_peca(peca_para_str(j)[1:2])

#TAD Tabuleiro

def cria_tabuleiro():
    tabuleiro = {
        'a1':0, 'b1':0, 'c1':0,
        'a2':0, 'b2':0, 'c2':0,
        'a3':0, 'b3':0, 'c3':0
    }

    return tabuleiro

def cria_copia_tabuleiro(t):
    return t

def obter_peca(t, p):
    return t[posicao_para_str(p)]

def obter_vetor(t, s):
    if s == 'a':
        return (t['a1'], t['a2'], t['a3'])
    elif s == 'b':
        return (t['b1'], t['b2'], t['b3'])
    elif s == 'c':
        return (t['c1'], t['c2'], t['c3'])
    elif s == '1':
        return (t['a1'], t['b1'], t['c1'])
    elif s == '2':
        return (t['a2'], t['b2'], t['c2'])
    elif s == '3':
        return (t['a3'], t['b3'], t['c3'])

#soma todos os valores de um vetor
def soma_pecas_em_linha(t,s):
    soma = 0
    soma = sum(obter_vetor(t,s))
    return soma

#soma todos os valores de todas as linhas e colunas
def todas_soma_pecas_em_linha(t):
    listaTodas = ['a', 'b', 'c', '1', '2', '3']
    listaNova = []
    for i in listaTodas:
        listaNova.append(soma_pecas_em_linha(t,i))
    return listaNova

def coloca_peca(t,j,p):
    t[posicao_para_str(p)] = peca_para_inteiro(j)
    return t

def remove_peca(t, p):
    t[posicao_para_str(p)] = ' '
    return t

def mais_que_um_vencedor(t):
    lista = todas_soma_pecas_em_linha(t)

def move_peca(t, p1, p2):
    t[posicao_para_str(p2)] = obter_peca(t, p1)
    t[posicao_para_str(p1)] = 0
    return t

def eh_tabuleiro(t):
    sumTotal = 0
    sumSmall = 0
    properList = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

    if sorted(list(t)) != sorted(properList):
        return False
    
    if obter_ganhador(t) == False:
        return False

    for key in t:  
        sumTotal += abs(t[key])
        sumSmall += t[key]
        
        #verifica se tem um máximo de 3 peças de cada jogador
        #atraves da soma dos modulos dos valores
        if sumTotal > 6:
            return False
        #verifica se um jogador tem mais peças que o outro
        #atraves do modulo da soma dos valores
        if abs(sumSmall) > 1:
            return False

        if not -1 <= t[key] <= 1:
            return False

    return True
    
def eh_posicao_livre(t,p):
    return obter_peca(t,p) == 0

#def tabuleiros_iguais
def tabuleiros_iguais(t1, t2):
    return t1 == t2
    
#def tabuleiro_para_str
def tabuleiro_para_str(t):
    stringTab = """   a   b   c
1 --
   | \ | / |
2 --
   | / | \ |
3 --"""

    return stringTab[:15] + peca_para_str(t['a1']) + stringTab[15:16] + \
    peca_para_str(t['b1']) + stringTab[16:17] + peca_para_str(t['c1']) + \
    stringTab[17:33] + peca_para_str(t['a2']) + stringTab[33:34] + \
    peca_para_str(t['b2']) + stringTab[34:35] + peca_para_str(t['c2']) + \
    stringTab[35:51] + peca_para_str(t['a3']) + stringTab[51:52] + \
    peca_para_str(t['b3']) + stringTab[52:53] + peca_para_str(t['c3'])
    
#def tuplo_para_tabuleiro

def tuplo_para_tabuleiro(t):
    tabuleiro = cria_tabuleiro()
    tabuleiro['a1'] = t[0][0]
    tabuleiro['b1'] = t[0][1]
    tabuleiro['c1'] = t[0][2]
    tabuleiro['a2'] = t[1][0]
    tabuleiro['b2'] = t[1][1]
    tabuleiro['c2'] = t[1][2]
    tabuleiro['a3'] = t[2][0]
    tabuleiro['b3'] = t[2][1]
    tabuleiro['c3'] = t[2][2]
    return tabuleiro

def obter_ganhador(t): 
    lista = todas_soma_pecas_em_linha(t)
    nump3 = 0
    numn3 = 0

    if 3 in lista:
        nump3 += 1

    if -3 in lista:
        numn3 += 1

    #Devolve falso se houver 2 ganhadores
    if numn3 == nump3:
        return False

    if 3 in lista:
        return cria_peca('X')
    elif -3 in lista:
        return cria_peca('O')
    else:
        return cria_peca(' ')

def obter_posicoes_livres(t):
    tuploPos = ()
    for i in t:
        if t[i] == 0:
            tuploPos += (i,)

    return tuploPos

def obter_posicoes_jogador(t,j):
    tuploPos = ()
    for i in t:
        if t[i] == peca_para_inteiro(j):
            tuploPos += (i,)

