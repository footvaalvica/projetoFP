dinheiro = float(input("Insira a quantia de dinheiro\n"))

resto = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
moedas2 = 0
moedas1 = 0
moedas50 = 0
moedas20 = 0
moeadas10 = 0
moedas5 = 0
moedas2 = 0
moedas1 = 0

while dinheiro > 0:
    notas50 = dinheiro // 50
    resto = dinheiro % 50
    dinheiro = dinheiro - resto
    notas20 = dinheiro // 20
    resto = dinheiro % 20
    dinheiro = dinheiro - resto
    notas10 = dinheiro // 10
    resto = dinheiro % 10
    dinheiro = dinheiro - resto
    notas5 = dinheiro // 5
    resto = dinheiro % 5
    dinheiro = dinheiro - resto
    moedas2 = dinheiro // 2
    resto = dinheiro % 2
    dinheiro = dinheiro - resto
    moedas1 = dinheiro // 1
    resto = dinheiro % 1
    dinheiro = dinheiro - resto
    moedas50 = dinheiro // 0.5
    resto = dinheiro % 0.5
    dinheiro = dinheiro - resto
    moedas20 = dinheiro // 0.2
    resto = dinheiro % 0.2
    dinheiro = dinheiro - resto
    moedas10 = dinheiro // 0.1
    resto = dinheiro % 0.1
    dinheiro = dinheiro - resto
    moedas5 = dinheiro // 0.05
    resto = dinheiro % 0.05
    dinheiro = dinheiro - resto
    moedas2 = dinheiro // 0.02
    resto = dinheiro % 0.02
    dinheiro = dinheiro - resto
    moedas1 = dinheiro // 0.01
    resto = dinheiro % 0.01
    dinheiro = dinheiro - resto

print(notas50,
notas20,
notas10,
notas5,
moedas2,
moedas1,
moedas50,
moedas20,
moeadas10,
moedas5,
moedas2,
moedas1)
