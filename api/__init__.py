from flask import Blueprint
from flask import render_template, request
api_bp = Blueprint('api_bp', __name__, template_folder='templates')

from . import product
