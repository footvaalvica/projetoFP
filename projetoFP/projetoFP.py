#Mateus Leite Pinho ist199282

##############################################################################
#                                     INICIO                                 #
##############################################################################

##############################################################################
#                                  TAD POSICAO                               #
##############################################################################

#TAD posicao
#Representacao interna: lista de dois elementos ([coluna, linha])
# cria_posicao: str x str -> posicao
# cria_posicao: posicao -> posicao
# eh_posicao: universal -> booleano
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# posicoes_iguais: posicao x posicao -> str
# posicao_para_str: posicao -> str

def cria_posicao(c,l):
    """
    cria_posicao: str x str -> posicao

    recebe duas cadeias de carateres correspondentes a coluna c e a 
    linha l de uma posicao e devolve a posic ao correspondente
    """
    
    if type(c) == type(l) == str and len(c) == len(l) == 1 and \
    97 <= ord(c) <= 99 and 3 >= int(l) > 0:
        return [c,l]
    else:
        raise ValueError('cria_posicao: argumentos invalidos')

def obter_pos_c(p):
    """
    obter_pos_c: posicao -> str

    devolve a componente coluna c da posicao p
    """
    return p[0]

def obter_pos_l(p):
    """
    obter_pos_l: posicao -> str
    
    devolve a componente linha l da posicao p
    """
    return p[1]

def cria_copia_posicao(p):
    """
    cria_copia_posicao: posicao -> posicao
    
    recebe uma posicao e devolve uma copia nova da posicao
    """
    return p.copy()

def eh_posicao(p):
    """
    eh_posicao: universal -> booleano

    devolve True caso o seu argumento seja um TAD posicao e false
    caso contrario
    """
    return isinstance(p, list) and len(p) == 2 and type(p[0]) == \
    type(p[1]) == str and 97 <= ord(p[0]) <= 99 and 3 >= int(p[1]) > 0

def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao x posicao -> booleano

    devolve True apenas se p1 e p2 sao posicoes e sao iguais
    """
    return p1 == p2 and eh_posicao(p1) and eh_posicao(p2)

def posicao_para_str(p):
    """
    posicao_para_str: posicao -> str

    devolve a cadeia de caracteres 'cl' que representa o seu
    argumento, sendo os valores c e l as componentes coluna e linha de p
    """
    return str(obter_pos_c(p) + obter_pos_l(p))


##############################################################################
#                           FUNCOES CRIADAS POR MIM                          #
##############################################################################

def str_para_posicao(s):
    """ 
    str_para_posicao: str -> posicao
    
    devolve a posicao que corresponde a string 'cl'
    """
    return cria_posicao(s[:1], s[1:])

##############################################################################
#                         FUNCOES ALTO NIVEL POSICAO                         #
##############################################################################

def obter_posicoes_adjacentes(p):
    """
    obter_posicoes_adjacentes: posicao -> tuplo de posicoes

    devolve um tuplo com as posicoes adjacentes a posicao p de acordo
    com a ordem de leitura do tabuleiro
    """
    posicoes = {
        'a1':(['b','1'], ['a', '2'], ['b','2']),
        'a2':(['a','1'], ['b', '2'], ['a','3']),
        'a3':(['a','2'], ['b', '2'], ['b','3']),
        'b1':(['a','1'], ['c', '1'], ['b','2']),
        'b2':(['a','1'], ['b', '1'], ['c', '1'],
              ['a','2'], ['c', '2'], ['a', '3'],
              ['b','3'], ['c', '3']),
        'b3':(['b','2'], ['a', '3'], ['c','3']),
        'c1':(['b','1'], ['b', '2'], ['c','2']),
        'c2':(['c','1'], ['b', '2'], ['c','3']),
        'c3':(['b','2'], ['c', '2'], ['b','3'])
    }
    
    return posicoes[posicao_para_str(p)]

##############################################################################
#                                   TAD PECA                                 #
##############################################################################

#TAD peca
#Representacao da peca: 1 ou 0 ou -1 ou 1.0 ou 0.0 ou -1.0
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booleano
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str
# peca_para_inteiro: peca -> N

def cria_peca(j):
    """
    cria_peca: str -> peca
    
    recebe uma cadeira de carateres corresponde ao identficador
    de um dos dois jogadores ('X' ou 'O') ou a uma peca livre (' ')
    e devolve a peca correspondente
    """
    if j == 'X':
        return 1
    elif j == ' ':
        return 0
    elif j == 'O':
        return -1
    else:
        raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
    """
    cria_copia_peca: peca -> peca
    
    recebe uma peca e devolve uma copia nova da peca
    """
    return float(j)

def eh_peca(j):
    """
    eh_peca: universal -> booleano

    devolve True caso o seu argumento seja um TAD peca e False
    caso contrario
    """
    if j == 1:
        return True
    elif j == 0:
        return True
    elif j == -1:
        return True
    else:
        return False

def pecas_iguais(j1, j2):
    """
    pecas_iguais: peca x peca -> booleano

    devolve True apenas se p1 e p2 sao pecas e sao iguais
    """
    return j1 == j2 and eh_peca(j1) and eh_peca(j2)

def peca_para_str(j):
    """
    pecas_para_str: peca -> str

    devolve a cadeia de carateres que representa o jogador
    dono da peca, isto e, '[X]', '[O]' ou '[ ]'
    """
    if j == 1:
        return '[X]'
    if j == 0:
        return '[ ]'
    if j == -1:
        return '[O]'

##############################################################################
#                           FUNCOES CRIADAS POR MIM                          #
##############################################################################

def inteiro_para_peca(j):
    """
    inteiro_para_peca: int -> peca

    devolve 'X', ' ', 'O' para os inputs 1, 0, -1, respetivamente
    """
    if j == 1:
        return 'X'
    elif j == 0:
        return ' '
    elif j == -1:
        return 'O'

##############################################################################
#                            FUNCOES ALTO NIVEL PECA                         #
##############################################################################

def peca_para_inteiro(j):
    """
    peca_para_inteiro: peca -> N
    
    devolve um inteiro valor 1, -1 ou 0, dependendo se a peca e do
    jogador 'X', 'O' ou livre, respetivamente
    """
    return cria_peca(peca_para_str(j)[1:2])

##############################################################################
#                                TAD TABULEIRO                               #
##############################################################################

def cria_tabuleiro():
    tabuleiro = {
        'a1':cria_peca(' '), 
        'b1':cria_peca(' '), 
        'c1':cria_peca(' '),
        'a2':cria_peca(' '), 
        'b2':cria_peca(' '), 
        'c2':cria_peca(' '),
        'a3':cria_peca(' '), 
        'b3':cria_peca(' '), 
        'c3':cria_peca(' ')
    }
    return tabuleiro

def cria_copia_tabuleiro(t):
    t1 = t.copy()
    return t1

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

def coloca_peca(t,j,p):
    t[posicao_para_str(p)] = peca_para_inteiro(j)
    return t

def remove_peca(t, p):
    t[posicao_para_str(p)] = cria_peca(' ')
    return t

def move_peca(t, p1, p2):
    tempPeca = obter_peca(t, p1)
    t[posicao_para_str(p1)] = cria_peca(' ')
    t[posicao_para_str(p2)] = tempPeca
    return t

def eh_tabuleiro(t):
    sumTotal = 0
    sumSmall = 0
    properList = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

    if sorted(list(t)) != sorted(properList) and len(t) != len(properList):
        return False
    
    if ver_2_ganhadores(t) == True:
        return False

    for key in t:  
        sumTotal += abs(t[key])
        sumSmall += t[key]

        if type(key) != int:
            return False

        #verifica se tem um maximo de 3 pecas de cada jogador
        #atraves da soma dos modulos dos valores
        if sumTotal > 6:
            return False
        #verifica se um jogador tem mais pecas que o outro
        #atraves do modulo da soma dos valores
        if abs(sumSmall) > 1:
            return False

        if not -1 <= t[key] <= 1:
            return False

    return True
    
def eh_posicao_livre(t,p):
    return obter_peca(t,p) == cria_peca(' ')

def tabuleiros_iguais(t1, t2):
    return t1 == t2

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

def tuplo_para_tabuleiro(t):
    tabuleiro = cria_tabuleiro()
    tabuleiro['a1'] = cria_peca(inteiro_para_peca(t[0][0]))
    tabuleiro['b1'] = cria_peca(inteiro_para_peca(t[0][1]))
    tabuleiro['c1'] = cria_peca(inteiro_para_peca(t[0][2]))
    tabuleiro['a2'] = cria_peca(inteiro_para_peca(t[1][0]))
    tabuleiro['b2'] = cria_peca(inteiro_para_peca(t[1][1]))
    tabuleiro['c2'] = cria_peca(inteiro_para_peca(t[1][2]))
    tabuleiro['a3'] = cria_peca(inteiro_para_peca(t[2][0]))
    tabuleiro['b3'] = cria_peca(inteiro_para_peca(t[2][1]))
    tabuleiro['c3'] = cria_peca(inteiro_para_peca(t[2][2]))
    return tabuleiro

##############################################################################
#                           FUNCOES CRIADAS POR MIM                          #
##############################################################################

#soma todos os valores de um vetor
#nao respeita abstracao
def soma_pecas_em_linha(t,s):
    soma = 0
    soma = sum(obter_vetor(t,s))
    return soma

#soma todos os valores de todas as linhas e colunas
#nao respeita abstracao
def todas_soma_pecas_em_linha(t):
    listaTodas = ['a', 'b', 'c', '1', '2', '3']
    listaNova = []
    for i in listaTodas:
        listaNova.append(soma_pecas_em_linha(t,i))
    return listaNova

def ver_2_ganhadores(t):
    lista = todas_soma_pecas_em_linha(t)
    nump3 = 0
    numn3 = 0

    if 3 in lista:
        nump3 += 1

    if -3 in lista:
        numn3 += 1

    #Devolve verdadeiro se houver 2 ganhadores
    if numn3 == nump3 and numn3 != 0:
        return True

def sortedHelper(obj):
    helpfulTuple = (['a', '1'], ['b', '1'], ['c', '1'], 
    ['a', '2'], ['b', '2'], ['c', '2'], 
    ['a', '3'], ['b', '3'], ['c', '3'])
    i = 0

    while helpfulTuple[i] != obj:
        i += 1

    return i

##############################################################################
#                       FUNCOES ALTO NIVEL TABULEIRO                         #
##############################################################################

def obter_ganhador(t): 
    lista = todas_soma_pecas_em_linha(t)

    if 3 in lista:
        return cria_peca('X')
    elif -3 in lista:
        return cria_peca('O')
    else:
        return cria_peca(' ')

def obter_posicoes_livres(t):
    return obter_posicoes_jogador(t, cria_peca(' '))

#FUNCAO ALTO NIVEL MAS NAO RESPEITA ABSTRACAO
def obter_posicoes_jogador(t,j):
    listTuploPos = []
    for i in t:
        if t[i] == peca_para_inteiro(j):
            listTuploPos.append([i[0],i[1]])

    return tuple(sorted(listTuploPos, key=sortedHelper))

##############################################################################
#                                LOGICA DO JOGO                              #
##############################################################################

def obter_movimento_manual(t,j):
    if len(obter_posicoes_livres(t)) > 3:
        pos = input('Turno do jogador. Escolha uma posicao: ')
        if pos not in tuple(posicao_para_str(p) for p in \
        obter_posicoes_livres(t)):
            raise ValueError("obter_movimento_manual: escolha invalida")
        else:
            return (str_para_posicao(pos),)
    else:
        mov = input('Turno do jogador. Escolha um movimento: ')
        p1 = mov[:2]
        p2 = mov[2:]
        if p1 == p2:
            return "skip"
        else:
            if (p2 not in tuple(posicao_para_str(p) for p 
            in obter_posicoes_livres(t)) or t[p1] != j):
                raise ValueError("obter_movimento_manual: escolha invalida")
            else:
                return (str_para_posicao(p1), str_para_posicao(p2))

def obter_movimento_auto(t,j,s):
    #devolve tuplo
    if s == 'facil':
        if len(obter_posicoes_livres(t)) > 3:          
            return colocacao(t,j)
        else:
            return movimentoFacil(t,j)

    elif s == 'normal':
        if len(obter_posicoes_livres(t)) > 3:       
           return colocacao(t,j)
        else:
            result = minimax(t,j,1)
            if result[0] != 0:
                choppedResult = result[1]
                listPos = []
                for i in choppedResult:
                    listPos.append(cria_posicao(i[0], i[1]))
                return tuple(listPos)
            else:
                return movimentoFacil(t,j)

    elif s == 'dificil':
        if len(obter_posicoes_livres(t)) > 3:          
            return colocacao(t,j)
        else:
            result = minimax(t,j,5)
            choppedResult = result[1][:2]
            listPos = []
            for i in choppedResult:
                listPos.append(cria_posicao(i[0], i[1]))
            return tuple(listPos)

def movimentoFacil(t,j):
    for i in obter_posicoes_jogador(t,j):
        for e in obter_posicoes_adjacentes(i):
            if e in obter_posicoes_livres(t):
                return (cria_posicao(i[0],i[1]), cria_posicao(e[0],e[1]))

def colocacao(t,j):
    #VITORIA
    result = vitoria(t,j)
    if result is not None:
        return vitoria(t,j)
    #BLOQUEIO, igual a vitoria mas com -j
    result = vitoria(t,-j)
    if result is not None:
        return vitoria(t,-j)
    #CENTRO
    if 'b2' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('b', '2'),)
    #CANTOVAZIO
    if 'a1' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('a', '1'),)
    if 'c1' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('c', '1'),)
    if 'a3' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('a', '3'),)
    if 'c3' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('c', '3'),)
    #LATERALVAZIO
    if 'b1' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('b', '1'),)
    if 'a2' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('a', '2'),)
    if 'c2' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('c', '2'),)
    if 'b3' in tuple(posicao_para_str(p) for p in obter_posicoes_livres(t)):
        return (cria_posicao('b', '3'),)

def vitoria(t,j):
    LettersList = ['a', 'b', 'c']
    numbersList = ['1', '2', '3']

    for i in LettersList:
        vetorLista = list(obter_vetor(t,i))
        vetorListaCopy = vetorLista.copy()
        if 0 in vetorLista:
            vetorListaCopy.pop(vetorListaCopy.index(0))
        if 0 in vetorLista and vetorListaCopy[0] == vetorListaCopy[1] == j:
            return (cria_posicao(i,(str(obter_vetor(t,i).index(0)+1))),)

    for i in numbersList:
        vetorLista = list(obter_vetor(t,i))
        vetorListaCopy = vetorLista.copy()
        if 0 in vetorLista:
            vetorListaCopy.pop(vetorListaCopy.index(0))
        if 0 in vetorLista and vetorListaCopy[0] == vetorListaCopy[1] == j:
            return (cria_posicao(chr(((obter_vetor(t,i).index(0)+97))),i),)
    
def minimax(t,j,depth,*seq):
    if obter_ganhador(t) != 0 or depth == 0:
        return obter_ganhador(t), seq
    else:
        bestResult = -obter_ganhador(t)
        melhorSeqMovimentos = ()
        for i in obter_posicoes_jogador(t,j):
            for e in obter_posicoes_adjacentes(i):
                if e in obter_posicoes_livres(t):
                    novoTabuleiro = cria_copia_tabuleiro(t)
                    novoMovimento = str(posicao_para_str(i)), \
                    str(posicao_para_str(e))
                    novoTabuleiro = move_peca(novoTabuleiro, 
                    posicao_para_str(i), 
                    posicao_para_str(e))
                    novoResultado,novaSeqMovimentos = \
                    minimax(novoTabuleiro, -j, depth-1, *(seq+novoMovimento))
                    if melhorSeqMovimentos == () \
                    or (j == cria_peca('X') and novoResultado > bestResult) \
                    or (j == cria_peca('O') and novoResultado < bestResult):
                        bestResult, melhorSeqMovimentos = \
                        novoResultado,novaSeqMovimentos
        return bestResult,melhorSeqMovimentos

def moinho(peca, dif):
    #AUXILIAR 1
    def part1(t,j):
        move = obter_movimento_manual(t,j)
        if move == "skip":
            pass
        else:
            if len(move) == 1:
                t = coloca_peca(t,j,cria_posicao(move[0][0], move[0][1]))
            if len(move) == 2:
                t = move_peca(t, (cria_posicao(move[0][0], move[0][1])), 
                    (cria_posicao(move[1][0], move[1][1])))
            print(tabuleiro_para_str(t))

    #AUXILIAR 2
    def part2(t,j, dif):
        move = obter_movimento_auto(t,-j,dif)
        if len(move) == 1:
                t = coloca_peca(t,-j,cria_posicao(move[0][0], move[0][1]))
        if len(move) == 2:
                t = move_peca(t, (cria_posicao(move[0][0], move[0][1])), 
                (cria_posicao(move[1][0], move[1][1])))
        print("Turno do computador (" + dif + "):")
        print(tabuleiro_para_str(t))
    
    t = cria_tabuleiro()
    j = cria_peca(peca[1:2])
    gameActive = True
    ganhador = 0
    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + dif + ".")
    print(tabuleiro_para_str(t))
    if j == 1:
        while gameActive:
            part1(t,j)
            ganhador = obter_ganhador(t)
            if ganhador != 0:
                    return (peca_para_str(ganhador))
            part2(t,j,dif)
            ganhador = obter_ganhador(t)
            if ganhador != 0:
                return (peca_para_str(ganhador))
    if j == -1:
        while gameActive:
            part2(t,j,dif)
            ganhador = obter_ganhador(t)
            if ganhador != 0:
                return (peca_para_str(ganhador))
            part1(t,j)
            ganhador = obter_ganhador(t)
            if ganhador != 0:
                    return (peca_para_str(ganhador))

##############################################################################
#                                      FIM                                   #
##############################################################################            