from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session
from database.db import users

login_route = Blueprint("login", __name__)

@login_route.route('/')
def login():
    error_message = session.get('error')
    session.pop('error', None) 
    return render_template('login.html', error=error_message)

@login_route.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuariologin')
    passw = request.args.get('passwlogin')
    
    session.pop('error', None)  
    print(usuario, users)
    if usuario in users:
        if users[usuario] == passw:
            return render_template('home.html')
        else:
            session['error'] = "Senha incorreta. Tente novamente."
    else:
        session['error'] = "Usuário não encontrado."
    
    return redirect(url_for('login.login'))

@login_route.route('/new', methods=['GET'])
def register():
    pass

@login_route.route('/dados', methods=['GET'])
def obter_dados():
    return jsonify(users)
