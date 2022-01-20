from app.models import db
from app.automovel.models import Automovel
from flask import Blueprint

carro_api = Blueprint('carro_api', __name__)

class Carro(Automovel):
    __tablename__ = 'carro'

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    lugares = db.Column(db.Integer)
    portas = db.Column(db.Integer)


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
            'lugares':self.lugares,
            'portas':self.lugares,
            'disponivel':self.disponivel


        }
    