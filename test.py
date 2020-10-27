def amigas(palavra1, palavra2):
    counter = 0
    i = 0
    for i in len(palavra1):
        if palavra1[i] == palavra2[i]:
            counter += 1
        else:
            pass
    return counter/len(palavra1)