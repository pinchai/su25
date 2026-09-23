from flask import Blueprint
from flask import render_template, request
admin_bp = Blueprint('admin_bp', __name__,
                        template_folder='templates')

from . import auth
from . import dashboard
from . import user

# Custom 429 Error Page
@admin_bp.errorhandler(429)
def ratelimit_handler(e):
    return render_template(
        "429.html",
        ip=request.remote_addr,
        error=str(e)
    ), 429
