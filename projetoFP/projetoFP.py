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

def move_peca(t, p1, p2):
    t[posicao_para_str(p2)] = obter_peca(t, p1)
    return t

def eh_tabuleiro(t):
    sumTotal = 0
    sumSmall = 0
    properList = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

    if sorted(list(t)) != sorted(properList):
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
    stringDSd = """   a   b   c
1 [ ]-[ ]-[ ]
   | \ | / |  
2 [ ]-[ ]-[ ]
   | / | \ |
3 [ ]-[ ]-[ ]"""

    #acabar de fazer tabuleiro hardcoded

    return stringDSd

#def tuplo_para_tabuleiro

def obter_ganhador(t):
    lista = todas_soma_pecas_em_linha(t)
    if abs(sum(lista)) >= 3 and sum(lista) > 0:
        return cria_peca('X')
    elif abs(sum(lista)) >= 3 and sum(lista) < 0:
        return cria_peca('O')
    else:
        return cria_peca(' ')

#def obter_posicoes_livres

#def obter_posicoes_jogador