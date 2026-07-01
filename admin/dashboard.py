from . import admin_bp
from flask import render_template


@admin_bp.get('/dashboard')
def dashboard():
    return render_template('admin/master.html')