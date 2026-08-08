from . import admin_bp
from flask import render_template, request, redirect, url_for
from sqlalchemy import text
from extensions import db
from models.user import User


@admin_bp.get('/user')
def user():
    module = 'user'

    sql = text("SELECT * FROM user")
    result = db.session.execute(sql)
    rows = [dict(row._mapping) for row in result]

    return render_template(
        'admin/user/index.html',
        module=module,
        users=rows
    )


@admin_bp.get('/user/add')
def add_user():
    module = 'user'
    return render_template('admin/user/add.html', module=module)


@admin_bp.get('/user/edit/<int:user_id>')
def edit_user(user_id):
    module = 'user'
    return render_template(
        'admin/user/edit.html',
        module=module
    )


@admin_bp.get('/user/confirm-delete/<int:user_id>')
def confirm_delete(user_id):
    module = 'user'
    sql = text("SELECT * FROM user WHERE id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id}).fetchone()
    user = dict(result._mapping)

    return render_template(
        'admin/user/confirm_delete.html',
        module=module,
        user=user
    )


@admin_bp.post('/user/delete')
def user_delete():
    module = 'user'
    form = request.form
    user_id = form.get('user_id')
    user = User.query.get(user_id)
    if user is None:
        return redirect(url_for('admin_bp.user'))
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin_bp.user'))
