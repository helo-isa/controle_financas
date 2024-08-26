from flask import Blueprint, render_template

ganhos_route = Blueprint("ganhos", __name__)

@ganhos_route.route('/')
def ganhos():
    return render_template('ganhos.html')