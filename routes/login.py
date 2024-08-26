from flask import Blueprint, render_template

home_route = Blueprint("home", __name__)

@login_route.route('/')
def login():
    return render_template('login.html')