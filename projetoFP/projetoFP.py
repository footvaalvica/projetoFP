#Mateus Leite Pinho ist199282

def tabuleiroMelhor(tab):
    if eh_tabuleiro(tab) == True:
        tabuleiromelhor = ()
        for i in tab:
            tabuleiromelhor += i
        return tabuleiromelhor
    else:
        raise ValueError("boy we wasn't ever no joke")

def eh_tabuleiro(tab):
    Truth = False
    if isinstance(tab, tuple) and len(tab) == 3:
        for i in tab:
            if len(i) == 3:
                for i2 in i:
                    if i2 == 1 or i2 == 0 or i2 == -1:
                        Truth = True
                    else:
                        return False
            else:
                return False
    else:
        return False
    return Truth    

def eh_posicao(pos):
    return isinstance(pos, int) and 1 <= pos <= 9

def obter_coluna(tab, num):
    coluna = ()
    if (eh_tabuleiro(tab) and isinstance(num, int) and 1 <= num <= 3) == True:
        num -= 1
        for i in tab:
            coluna += (i[num],)
        return coluna
    else:
        raise ValueError("caca")

def obter_linha(tab, num):
    if (eh_tabuleiro(tab) and isinstance(num, int) and 1 <= num <= 3) == True:
        num -= 1
        return tab[num]
    else:
        raise ValueError("caca")

def obter_diagonal(tab, num):
    diagonal = ()
    if (eh_tabuleiro(tab) and isinstance(num, int) and 1 <= num <= 2) == True:
        if num == 1:
            diagonal += (tab[0][0],) + (tab[1][1],) + (tab[2][2],)
        if num == 2:
            diagonal += (tab[0][2],) + (tab[1][1],) + (tab[2][0],)
        return diagonal
    else:
        raise ValueError("caca")

def tabuleiro_str(tab):

    """A função está super macabra, basicamente estou a transformar a string numa lista
    e a inserir nas posições certas
    """

    tabGood2 = []
    tabPos = (1,5,9,25,29,33,49,53,57)
    counter = 0
    corda = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
    cordaList = []
    newCorda = ""
    if eh_tabuleiro(tab) == False:
        raise ValueError("caca")
    else:
        cordaList = list(corda)
        tabGood = tabuleiroMelhor(tab)
        for i in tabGood:
            if i == 1:
                i = "X"
            elif i == 0:
                i = " "
            elif i == -1:
                i = "O"
            tabGood2.append(i)
        while counter < len(tabGood2):
            cordaList[tabPos[counter]] = tabGood2[counter]
            counter += 1
        for i in cordaList:
            newCorda += str(i)
        print(newCorda)

def eh_posicao_livre(tab,pos):
    tabGood = tabuleiroMelhor(tab)
    if eh_tabuleiro(tab) == False and eh_posicao(pos) == False:
        raise ValueError("eh_posicao_livre:  algum dos argumentos e invalido")
    else:
        counter = 0
        while counter < len(tabGood):
            if counter == pos and tabGood[counter] == 0:
                return True
            counter += 1
        return False

def obter_posicoes_livres(tab):
    tuploPosicoesLivres = ()
    if eh_tabuleiro(tab) == False:
        raise ValueError("obter_posicoes_livres:  o argumento e invalido")
    for i in range(9):
        if eh_posicao_livre(tab,(i+1)) == True:
            tuploNovo += ((i+1),)
    return tuploPosicoesLivres

def jogador_ganhador(tab):
    if eh_tabuleiro(tab) == False:
        raise ValueError("jogador_ganhador:  o argumento e invalido")
    else:
        for i in range(3):
            if obter_linha(tab,i+1) == (1,1,1):
                return 1
            if obter_linha(tab,i+1) == (-1,-1,-1):
                return -1
            if obter_linha(tab,i+1) == (0,0,0):
                return 0
        for i in range(3):
            if obter_coluna(tab,i+1) == (1,1,1):
                return 1
            if obter_coluna(tab,i+1) == (-1,-1,-1):
                return -1
            if obter_coluna(tab,i+1) == (0,0,0):
                return 0
        for i in range(2):
            if obter_diagonal(tab,i+1) == (1,1,1):
                return 1
            if obter_diagonal(tab,i+1) == (-1,-1,-1):
                return -1
            if obter_diagonal(tab,i+1) == (0,0,0):
                return 0

def marcar_posicao(tab,n,pos):
    pass