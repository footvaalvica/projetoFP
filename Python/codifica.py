def codifica(texto):
    str1 = ""
    str2 = ""
    i = 0
    while i < len(texto):
        if i % 2 == 0:
            str2 = str2 + texto[i]
        else:
            str1 = str1 + texto[i]
        i += 1
    return (str1 + str2)

def descodifica(texto):
    pass