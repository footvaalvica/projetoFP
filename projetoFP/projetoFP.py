#Mateus Leite Pinho ist199282

def tabuleiroMelhor(tab):
    if eh_tabuleiro(tab) == True:
        tabuleiromelhor = ()
        for i in tab:
            tabuleiromelhor += i
        return tabuleiromelhor
    else:
        raise ValueError("boy we wasn't ever no joke")

def eh_tabuleiro(tab, *therest):
    Truth = False
    if isinstance(tab, tuple) and len(tab) == 3:
        for i in tab:
            if len(i) == 3:
                for i2 in i:
                    if isinstance(i2,bool) == False and (i2 == 1 or i2 == 0 or i2 == -1):
                        Truth = True
                    else:
                        return False
            else:
                return False
    else:
        return False
    return Truth    

def eh_posicao(pos):
    return isinstance(pos,bool) == False and isinstance(pos, int) and 1 <= pos <= 9

def obter_coluna(tab, num):
    coluna = ()
    if isinstance(num,bool) == False and (eh_tabuleiro(tab) and isinstance(num, int) and 1 <= num <= 3) == True:
        num -= 1
        for i in tab:
            coluna += (i[num],)
        return coluna
    else:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")

def obter_linha(tab, num):
    if isinstance(num,bool) == False and (eh_tabuleiro(tab) and isinstance(num, int) and 1 <= num <= 3) == True:
        num -= 1
        return tab[num]
    else:
        raise ValueError("obter_linha: algum dos argumentos e invalido")

def obter_diagonal(tab, num):
    diagonal = ()
    if isinstance(num,bool) == False and (eh_tabuleiro(tab) and isinstance(num, int) and 1 <= num <= 2) == True:
        if num == 1:
            diagonal += (tab[0][0],) + (tab[1][1],) + (tab[2][2],)
        if num == 2:
            diagonal += (tab[2][0],) + (tab[1][1],) + (tab[0][2],)
        return diagonal
    else:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")

def tabuleiro_str(tab):
    """
    A funcao esta super macabra, basicamente estou a transformar a string numa lista
    e a inserir nas posicoes certas
    """
    tabComX = []
    tabPos = (1,5,9,25,29,33,49,53,57)
    counter = 0
    corda = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
    newCorda = ""
    if eh_tabuleiro(tab) == False:
        raise ValueError("tabuleiro_str: o argumento e invalido")
    corda = list(corda)
    tabGood = tabuleiroMelhor(tab)
    for i in tabGood:
        if i == 1:
            i = "X"
        elif i == 0:
            i = " "
        elif i == -1:
            i = "O"
        tabComX.append(i)
    while counter < len(tabComX):
        corda[tabPos[counter]] = tabComX[counter]
        counter += 1
    for i in corda:
        newCorda += str(i)
    return newCorda

def eh_posicao_livre(tab,pos):
    tabGood = tabuleiroMelhor(tab)
    if eh_tabuleiro(tab) == False or eh_posicao(pos) == False:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    else:
        counter = 0
        while counter < len(tabGood):
            if (counter + 1) == pos and tabGood[counter] == 0:
                return True
            counter += 1
        return False

def obter_posicoes_livres(tab):
    tuploPosicoesLivres = ()
    if eh_tabuleiro(tab) == False:
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    for i in range(9):
        if eh_posicao_livre(tab,(i+1)) == True:
            tuploPosicoesLivres += ((i+1),)
    return tuploPosicoesLivres

def jogador_ganhador(tab):
    if eh_tabuleiro(tab) == False:
        raise ValueError("jogador_ganhador: o argumento e invalido")
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
        return 0
    return 0

def marcar_posicao(tab,n,pos):
    if eh_posicao_livre(tab,pos) == False or isinstance(n,bool) == True or (n != 1 and n != -1):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")
    else:
        tabGood = tabuleiroMelhor(tab)
        tabGood = list(tabGood)
        tabGood[pos-1] = n
    return tuple(tabGood[:3]),tuple(tabGood[3:6]),tuple(tabGood[6:9])

def escolher_posicao_manual(tab):
    if eh_tabuleiro(tab) == False:
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    try:
        x = int(input("Turno do jogador. Escolha uma posicao livre: "))
    except:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    if eh_posicao_livre(tab,x) == False:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    return x

def escolher_posicao_auto(tab,n,strat):
    def vitoria1(tab,n):
        pos = 0
        for i in range(3):
            linha = obter_linha(tab,(i+1))
            if linha[0] != 0 and linha[0] == linha[2] and linha[1] == 0:
                pos = 2 + 3*i
                marcar_posicao(tab,n,pos)
                return pos
            elif linha[0] != 0 and linha[0] == linha[1] and linha[2] == 0:
                pos = 3 + 3*i
                marcar_posicao(tab,n,pos)
                return pos
            elif linha[1] != 0 and linha[1] == linha[2] and linha[0] == 0:
                pos = 1 + 3*i
                marcar_posicao(tab,n,pos)
                return pos
            coluna = obter_coluna(tab,(i+1))
            if coluna[0] != 0 and coluna[0] == coluna[2] and coluna[1] == 0:
                pos = 4 + i
                marcar_posicao(tab,n,pos)
                return pos
            elif coluna[0] != 0 and coluna[0] == coluna[1] and coluna[2] == 0:
                pos = 7 + i
                marcar_posicao(tab,n,pos)
                return pos
            elif coluna[1] != 0 and coluna[1] == coluna[2] and coluna[0] == 0:
                pos = 1 + i
                marcar_posicao(tab,n,pos)
                return pos
        for i in range(2):
            diagonal = obter_diagonal(tab,i+1)
            if diagonal[0] != 0 and diagonal[0] == diagonal[2] and diagonal[1] == 0:
                marcar_posicao(tab,n,5)
                return 5
            elif diagonal[0] != 0 and diagonal[0] == diagonal[1] and diagonal[2] == 0:
                pos = 9 - 6*i
                marcar_posicao(tab,n,pos)
                return pos
            elif diagonal[1] != 0 and diagonal[1] == diagonal[2] and diagonal[0] == 0:
                pos = 1 + 6*i
                marcar_posicao(tab,n,pos)
                return pos
        return pos

    def bloqueio2(tab,n):
        pos = 0
        for i in range(3):
            linha = obter_linha(tab,(i+1))
            if linha[1] != 0 and linha[1] == -n:
                if linha[0] == linha[1] and linha[2] == 0:
                    pos = 3+3*i
                    marcar_posicao(tab,n,pos)
                    return pos
                if linha[1] == linha[2] and linha[0] == 0:
                    pos = 1+3*i
                    marcar_posicao(tab,n,pos)
                    return pos
            coluna = obter_coluna(tab,(i+1))
            if coluna[1] != 0 and linha[1] == -n:
                if coluna[0] == coluna[1] and coluna[2] == 0:
                    pos = 7+i
                    marcar_posicao(tab,n,pos)
                    return pos
                if coluna[1] == coluna[2] and coluna[0] == 0:
                    pos = 1+i
                    marcar_posicao(tab,n,pos)
                    return pos
        for i in range(2):
            diagonal = obter_diagonal(tab,i+1)
            if diagonal[1] != 0 and diagonal[1] == -n:
                if diagonal[0] == diagonal[1] and diagonal[2] == 0:
                    pos = 9 - 6*i
                    marcar_posicao(tab,n,pos)
                    return pos
                if diagonal[1] == diagonal[2] and diagonal[0] == 0:
                    pos = 1 + 6*i
                    marcar_posicao(tab,n,pos)
                    return pos
        return pos
        
    #Falta definir

    def bifurcacao3(tab,n):
        pass

    def bloqueiobifurcacao4(tab,n):
        pass

    #Ja feitas

    def centro5(tab,n):
        if tab[1][1] == 0:
            marcar_posicao(tab,n,5)
            return 5
        return 0

    def cantooposto6(tab,n):
        if tab[0][0] == -n and tab[2][2] == 0:
            marcar_posicao(tab,n,9)
            return 9
        elif tab[0][2] == -n and tab[2][0] == 0:
            marcar_posicao(tab,n,7)
            return 7
        elif tab[2][0] == -n and tab[0][2] == 0:
            marcar_posicao(tab,n,3)
            return 3
        elif tab[2][2] == -n and tab[0][0] == 0:
            marcar_posicao(tab,n,1)
            return 1
        return 0

    def cantovazio7(tab,n):
        if tab[0][0] == 0:
            marcar_posicao(tab,n,1)
            return 1
        elif tab[0][2] == 0:
            marcar_posicao(tab,n,3)
            return 3
        elif tab[2][0] == 0:
            marcar_posicao(tab,n,7)
            return 7
        elif tab[2][2] == 0:
            marcar_posicao(tab,n,9)
            return 9
        return 0

    def lateralvazio8(tab,n):
        if tab[0][1] == 0:
            marcar_posicao(tab,n,2)
            return 2
        elif tab[1][0] == 0:
            marcar_posicao(tab,n,4)
            return 4
        elif tab[1][2] == 0:
            marcar_posicao(tab,n,6)
            return 6
        elif tab[2][1] == 0:
            marcar_posicao(tab,n,8)
            return 8
        return 0

    return_var = 0
    if eh_tabuleiro(tab) == False or isinstance(n,bool) == True or (n != 1 and n != -1) or (strat != 'basico' and strat != 'normal' and strat != 'perfeito'):
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")
    if strat == "basico":
        return_var = centro5(tab,n)
        if return_var != 0:
            return return_var
        return_var = cantovazio7(tab,n)
        if return_var != 0:
            return return_var
        return_var = lateralvazio8(tab,n)
        if return_var != 0:
            return return_var
    elif strat == "normal":
        return_var = vitoria1(tab,n)
        if return_var != 0:
            return return_var
        return_var = bloqueio2(tab,n)
        if return_var != 0:
            return return_var
        return_var = centro5(tab,n)
        if return_var != 0:
            return return_var
        return_var = cantooposto6(tab,n)
        if return_var != 0:
            return return_var
        return_var = cantovazio7(tab,n)
        if return_var != 0:
            return return_var
        return_var = lateralvazio8(tab,n)
        if return_var != 0:
            return return_var
    elif strat == "perfeito":
        return_var = vitoria1(tab,n)
        if return_var != 0:
            return return_var
        return_var = bloqueio2(tab,n)
        if return_var != 0:
            return return_var
        return_var = centro5(tab,n)
        if return_var != 0:
            return return_var
        return_var = cantooposto6(tab,n)
        if return_var != 0:
            return return_var
        return_var = cantovazio7(tab,n)
        if return_var != 0:
            return return_var
        return_var = lateralvazio8(tab,n)
        if return_var != 0:
            return return_var

def jogo_do_galo(jogador,strat):
    tab = ((0,0,0),(0,0,0),(0,0,0))
    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '" + jogador + "'.")
    if strat != 'basico' and strat != 'normal' and strat != 'perfeito':
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")
    if jogador == "O":
        while True:
            print("Turno do computador" + " (" + strat + "):")
            tab = marcar_posicao(tab,1,(escolher_posicao_auto(tab,1,strat)))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1:
                return '0'
            elif jogador_ganhador(tab) == 1:
                return 'X'
            tabGood = tabuleiroMelhor(tab)
            if 0 not in tabGood:
                return "EMPATE"
            x = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,-1,x)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1:
                return 'O'
            elif jogador_ganhador(tab) == 1:
                return 'X'
            tabGood = tabuleiroMelhor(tab)
            if 0 not in tabGood:
                return "EMPATE"            
    if jogador == "X":
        while True:
            x = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,1,x)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1:
                return '0'
            elif jogador_ganhador(tab) == 1:
                return 'X'
            tabGood = tabuleiroMelhor(tab)
            if 0 not in tabGood:
                return "EMPATE"
            print("Turno do computador" + " (" + strat + "):")
            tab = marcar_posicao(tab,-1,(escolher_posicao_auto(tab,1,strat)))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1:
                return 'O'
            elif jogador_ganhador(tab) == 1:
                return 'X'
            tabGood = tabuleiroMelhor(tab)
            if 0 not in tabGood:
                return "EMPATE"
    else:
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")