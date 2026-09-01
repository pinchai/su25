from models import User
from . import admin_bp
from flask import render_template, request, session, flash, redirect, url_for
from werkzeug.security import check_password_hash

from functools import wraps


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in first.", "warning")
            return redirect(url_for("admin_bp.admin_login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


@admin_bp.get('/login')
def admin_login():
    return render_template('admin/login.html', )


@admin_bp.post('/login')
def admin_do_login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()
        if not user:
            flash("Invalid username or password.", "danger")
            return redirect(url_for("admin_bp.admin_login"))

        if username == user.username and check_password_hash(user.password, password):
            session.clear()
            session["user_id"] = user.id
            session["username"] = user.username
            session["email"] = user.email
            session["profile"] = user.profile
            session["role"] = user.role
            flash("Welcome back!", "success")
            return redirect(request.args.get("next") or url_for("admin_bp.dashboard"))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for("admin_bp.admin_login"))
