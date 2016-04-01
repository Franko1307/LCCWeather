from flask import (Blueprint, render_template, abort, request, redirect,
                   current_app, redirect, url_for)
from .models import User, db
from .forms import LoginForm

mod = Blueprint('servidor_clima', __name__)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('alert_list'))
    return render_template('login.html')


@app.route('/alertas', methods=["GET", "POST"])
@login_required
def alert_list():
    return render_template('alerts.html')
