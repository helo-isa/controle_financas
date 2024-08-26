from flask import Blueprint, render_template

home_route = Blueprint("home", __name__)

@ganhos_route.route('/')
def ganhos():
    return render_template('ganhos.html')