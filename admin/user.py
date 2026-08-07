from . import admin_bp
from flask import render_template

@admin_bp.get('/user')
def user():
    module = 'user'
    return render_template(
        'admin/user/index.html',
        module=module
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
    return render_template(
        'admin/user/confirm_delete.html',
        module=module
    )