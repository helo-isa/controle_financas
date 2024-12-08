users = {
    'default': 'senha'
}

ganhos = [
]

despesas = [
]



def calcSaldo():
    saldo = 0
    for i in ganhos:
        saldo += i["value"]
    for i in despesas:
        saldo -= i["value"]
    return saldo

saldo = calcSaldo() 