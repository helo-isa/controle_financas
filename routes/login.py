from flask import Blueprint, render_template

login_route = Blueprint("login", __name__)

@login_route.route('/')
def login():
    return render_template('login.html')

@login_route.route('/', methods=['GET'])
def check_login():
    pass


@login_route.route('/new', methods=['GET'])
def register():
    pass