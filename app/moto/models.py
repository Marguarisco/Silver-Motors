from app.models import db
from app.automovel.models import Automovel
from flask import Blueprint

moto_api = Blueprint('moto_api', __name__)

class Moto(Automovel):
    __tablename__ = 'moto'

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)


    carrinho_compras = db.relationship('Carrinho_compras')

    def json(self):
        return{
            'placa':self.placa,
            'modelo':self.modelo,
            'cpf':self.cpf,
            'marca':self.marca,
            'ano':self.ano,
            'cor':self.cor,
            'valor':self.valor,
            'ipva':self.ipva,
            'quilometragem':self.quilometragem,
            'disponivel':self.disponivel,
        }
    