from . import front_bp
from flask import render_template, request


@front_bp.post('/create-user')
def create_user():
    form = request.form
    username = form['username']
    email = form['email']
    password = form['password']
    return 'created user'
