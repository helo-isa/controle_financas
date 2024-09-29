from flask import Blueprint, render_template
from database.db import saldo
home_route = Blueprint("home", __name__)

@home_route.route('/')
def home():
    return render_template('home.html', saldo=saldo)

