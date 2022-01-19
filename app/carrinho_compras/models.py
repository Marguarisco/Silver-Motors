from app.models import BaseModel, db
from flask import Blueprint

carrinho_compras_api = Blueprint('carrinho_compras_api', __name__)

class Carrinho_compras(BaseModel):
    __tablename__ = 'carrinho_compras'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.Integer)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    moto_id = db.Column(db.Integer, db.ForeignKey('moto.id')) 
    carro_id = db.Column(db.Integer, db.ForeignKey('carro.id')) 
    cupom_id = db.Column(db.Integer, db.ForeignKey('cupom.id'))  

    def json(self):
        return {
            'id':self.id,
            'valor':self.valor
        }