from flask import Blueprint, render_template, request
from database.db import users


login_route = Blueprint("login", __name__)

@login_route.route('/')
def login():
    return render_template('login.html')


@login_route.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    passw = request.args.get('passw')
    return "Usuario {} e senha{}".format(usuario,passw)
  



@login_route.route('/', methods=['GET'])
def check_login(user, passw):
    print(user, passw)
    if users[user]:
        if user[user] == passw:
            return render_template("login.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
@login_route.route('/new', methods=['GET'])
def register():
    pass