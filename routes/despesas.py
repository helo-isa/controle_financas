from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from database.db import despesas, saldo
despesas_route = Blueprint("despesas", __name__)

@despesas_route.route('/')
def listardespesas():
    return render_template('despesas.html', despesas=despesas, saldo=saldo)

@despesas_route.route('/', methods=['POST'])
def inserirdespesas():
    global saldo
    nova_despesa={
        "id": len(despesas) +1,
        "value": float(request.form.get('valor')),
        "class": request.form.get('categoria'),
        "date": request.form.get('data')
    }
    despesas.append(
        nova_despesa
    )
    saldo -= nova_despesa["value"]
    return render_template("despesas.html", despesas=despesas, saldo=saldo)

@despesas_route.route('/<int:despesa_id>/delete', methods=['DELETE'])
def deletardespesas(despesa_id):
    global despesas
    global saldo
    
    print("despesas antes da deleção:", despesas)
    
    for i in despesas:
        if despesa_id == i['id']:
            saldo += i['value']
    
    despesas = [u for u in despesas if u['id'] != despesa_id]
    print("despesas após a deleção:", despesas)

    # Retorne um JSON com o novo saldo
    return jsonify({"deleted": "ok", "novo_saldo": saldo})