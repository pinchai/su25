from models import User
from . import admin_bp
from flask import render_template, request, redirect, url_for
from sqlalchemy import text
from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash
from helpers.image import upload_image, delete_file
from .auth import login_required


@admin_bp.get('/user')
@login_required
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
@login_required
def add_user():
    module = 'user'
    return render_template('admin/user/add.html', module=module)


@admin_bp.post('/user/add/')
@login_required
def do_add_user():
    form = request.form
    file = request.files['image']
    file_name = upload_image(file=file)
    user = User(
        username=form.get('username'),
        email=form.get('email'),
        role=form.get('role'),
        password=generate_password_hash(form.get('password')),
        profile=file_name
    )

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('admin_bp.user'))


@admin_bp.get('/user/edit/<int:user_id>')
@login_required
def edit_user(user_id):
    module = 'user'
    sql = text("SELECT * FROM user WHERE id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id}).fetchone()
    user = dict(result._mapping)

    return render_template(
        'admin/user/edit.html',
        module=module,
        user=user
    )


@admin_bp.post('/user/edit/')
@login_required
def do_edit_user():
    module = 'user'
    form = request.form
    file = request.files['image']

    user_id = form.get('user_id')
    user = User.query.get(user_id)

    user.username = form.get('username')
    user.email = form.get('email')
    user.role = form.get('role')
    if form.get('password'):
        user.password = generate_password_hash(form.get('password'))
    if (file.filename).strip() != '':
        if user.profile is None:
            user.profile = upload_image(file=file)
        else:
            user.profile = upload_image(file=file, name=user.profile)

    db.session.commit()

    return redirect(url_for('admin_bp.user'))


@admin_bp.get('/user/confirm-delete/<int:user_id>')
@login_required
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
@login_required
def user_delete():
    module = 'user'
    form = request.form
    user_id = form.get('user_id')
    user = User.query.get(user_id)
    if user is None:
        return redirect(url_for('admin_bp.user'))

    # delete image
    if user.profile is not None:
        delete_file(user.profile)

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin_bp.user'))
