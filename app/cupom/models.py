from app.models import BaseModel, db
from flask import Blueprint

cupom_api = Blueprint('cupom_api', __name__)

class Cupom(BaseModel):
    __tablename__ = 'cupom'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    porcentagem = db.Column(db.Integer)
    data_expiracao = db.Column(db.Date)
    automovel_selecionado = db.Column(db.String(5))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id')) 


    def json(self):
        return {
            'id':self.id,
            'porcentagem':self.porcentagem,
            'data_expiracao':self.data_expiracao,
            'automovel_selecionado':self.automovel_selecionado
        }