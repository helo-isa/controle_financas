from flask import Blueprint, render_template

despesas_route = Blueprint("despesas", __name__)

@despesas_route.route('/')
def despesas():
    return render_template('despesas.html')
