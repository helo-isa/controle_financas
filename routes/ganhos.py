from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from database.db import ganhos, saldo
ganhos_route = Blueprint("ganhos", __name__)

@ganhos_route.route('/')
def listarganhos():
    return render_template('ganhos.html', ganhos=ganhos, saldo=saldo)

@ganhos_route.route('/', methods=['POST'])
def inserirganhos():
    global saldo
    novo_ganho={
        "id": len(ganhos) +1,
        "value": float(request.form.get('valor')),
        "class": request.form.get('categoria'),
        "date": request.form.get('data')
    }
    ganhos.append(
        novo_ganho
    )
    saldo += novo_ganho["value"]
    return render_template("ganhos.html", ganhos=ganhos, saldo=saldo)

@ganhos_route.route('/<int:ganho_id>/delete', methods=['DELETE'])
def deletarGanhos(ganho_id):
    global ganhos
    global saldo
    
    print("Ganhos antes da deleção:", ganhos)
    
    for i in ganhos:
        if ganho_id == i['id']:
            saldo -= i['value']
    
    ganhos = [u for u in ganhos if u['id'] != ganho_id]
    print("Ganhos após a deleção:", ganhos)

    # Retorne um JSON com o novo saldo
    return jsonify({"deleted": "ok", "novo_saldo": saldo})