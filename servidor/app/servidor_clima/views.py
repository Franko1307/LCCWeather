from flask import (Blueprint, render_template, abort, request, redirect,
                   current_app, redirect, url_for, flash)
from .forms import LoginForm
from .models import User
from flask.ext.login import (login_required, login_user, logout_user,
                             current_user)
from app import db, login_manager

mod = Blueprint('servidor_clima', __name__)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@mod.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    success = False
    if request.method == 'POST':
        if form.validate_on_submit():
            print("?")
            user = form.get_user()
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('.alert_list'))
        else:
            flash('Datos incorrectos', 'error')

    if current_user.is_authenticated:
        return redirect(url_for('.alert_list'))

    return render_template('login.html', form=form)


@mod.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('.login'))


@mod.route('/alertas', methods=["GET"])
@login_required
def alert_list():
    return render_template('alerts.html')


@mod.route('/exportar', methods=["GET"])
@login_required
def export_data():
    return render_template('export.html')
