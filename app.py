from flask import Flask, render_template, request
from product import product

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('front/home.html', product=product)


@app.get('/cart')
def cart():
    return render_template('front/cart.html')


@app.get('/checkout')
def checkout():
    return render_template('front/checkout.html')


@app.get('/detail')
def detail():
    pro_id = request.args.get('pro_id')
    title = request.args.get('title')
    image = request.args.get('image')
    price = request.args.get('price')
    description = request.args.get('description')

    return render_template('front/detail.html', pro_id=pro_id, title=title, image=image, price=price, description=description)


@app.post('/create-user')
def create_user():
    form = request.form
    username = form['username']
    email = form['email']
    password = form['password']
    return 'created user'


if __name__ == '__main__':
    app.run()
