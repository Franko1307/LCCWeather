from flask_wtf import Form, validators
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired
from app import db, bcrypt
from .models import User


def validate_login(form, field):
    user = form.get_user()

    if user is None:
        raise validators.ValidationError('Usuario invalido')
    if not bcrypt.check_password_hash(user.password, form.password.data):
        raise validators.ValidationError('Contraseña invalida')

    print('Kreygasm')


class LoginForm(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[
        DataRequired(), validate_login
    ])

    def get_user(self):
        return User.query.get(self.username.data)
