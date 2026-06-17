from . import front_bp
from flask import render_template
from product import product

@front_bp.get('/')
def home():
    return render_template('front/home.html', product=product)