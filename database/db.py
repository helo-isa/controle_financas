users = {
    'default': 'senha'
}

ganhos = [
{
    "id" : 1,
    "value": 50,
    "date": "20/09/2024",
    "class": "algo",
},
{
    "id": 3,
    "value": 100,
    "date": "22/09/2024",
    "class": "venda",
},
{
    "id": 4,
    "value": 150,
    "date": "23/09/2024",
    "class": "investimento",
},
{
    "id": 5,
    "value": 200,
    "date": "24/09/2024",
    "class": "bonus",
}
]

despesas = [
    {
        "id": 1,
        "value": 50,
        "date": "21/09/2024",
        "class": "alimentação",
    },
    {
        "id": 2,
        "value": 100,
        "date": "22/09/2024",
        "class": "transporte",
    },
    {
        "id": 3,
        "value": 120,
        "date": "23/09/2024",
        "class": "moradia",
    },
    {
        "id": 4,
        "value": 45,
        "date": "24/09/2024",
        "class": "lazer",
    },
]



def calcSaldo():
    saldo = 0
    for i in ganhos:
        saldo += i["value"]
    for i in despesas:
        saldo -= i["value"]
    return saldo

saldo = calcSaldo() 