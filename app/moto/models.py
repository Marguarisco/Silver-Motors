from app.models import BaseModel, db
from flask import Blueprint

moto_api = Blueprint('moto_api', __name__)

class Moto(BaseModel):
    __tablename__ = 'moto'

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    placa = db.Column(db.String(10), unique=True, index=True)
    modelo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    ano = db.Column(db.String(70))
    cor = db.Column(db.String(100))

    carrinho_compras = db.relationship('Carrinho_compras')

    def json(self):
        return{
            'placa':self.placa,
            'modelo':self.modelo,
            'cpf':self.cpf,
            'marca':self.marca,
            'ano':self.ano,
            'cor':self.cor
        }
    