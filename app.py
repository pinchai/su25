from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('front/home.html')


@app.get('/cart')
def cart():
    return render_template('front/cart.html')


@app.get('/checkout')
def checkout():
    return render_template('front/checkout.html')


@app.post('/create-user')
def create_user():
    form = request.form
    username = form['username']
    email = form['email']
    password = form['password']
    return 'created user'


if __name__ == '__main__':
    app.run()
