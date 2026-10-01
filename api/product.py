from . import api_bp
from product import product
from admin.auth import  login_required

@api_bp.get('/products')
def products_list():
    return product