from . import front_bp
from flask import render_template, request


@front_bp.get('/detail')
def detail():
    pro_id = request.args.get('pro_id')
    title = request.args.get('title')
    image = request.args.get('image')
    price = request.args.get('price')
    description = request.args.get('description')

    return render_template('front/detail.html', pro_id=pro_id, title=title, image=image, price=price,
                           description=description)
