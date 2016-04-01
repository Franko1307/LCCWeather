from db import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime
import random


class Lectura(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    humedad = Column(Integer)
    luz = Column(Integer, default=random.randint(1, 100))
    calidadaire = Column(Integer, default=random.randint(1, 100))
    nitrogeno = Column(Integer, default=random.randint(1, 100))
    monoxido = Column(Integer, default=random.randint(1, 100))
    temperatura = Column(Integer)
    presion = Column(Integer)

    def __init__(self, temperatura=None, presion=None, humedad=None):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad

    def __repr__(self):
        return '<User %r>' % (self.temperatura)


class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    """metodos requeridos por flask-login"""
    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
