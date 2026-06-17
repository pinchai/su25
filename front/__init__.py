from flask import Blueprint

front_bp = Blueprint('front_bp', __name__,
                        template_folder='templates')

from . import home
from . import cart
from . import checkout
from . import detail
from . import create_user

