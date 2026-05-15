from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from product import product

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
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
