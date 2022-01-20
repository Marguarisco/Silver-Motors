import email
from app.carrinho_compras.models import Carrinho_compras
from app.models import BaseModel, db
from flask import Blueprint

usuario_api = Blueprint('usuario_api', __name__)

class Usuario(BaseModel):
    __tablename__ = 'usuario'

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    sobrenome = db.Column(db.String(50))
    cpf = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(70), unique=True, index=True)
    rua = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    telefone = db.Column(db.String(13))
    sexo = db.Column(db.String(10))
    data_nascimento = db.Column(db.String(10))


    cupom = db.relationship('Cupom')
    carrinho_compras = db.relationship('Carrinho_compras')

    def json(self):
        return{
            'nome':self.nome,
            'sobrenome':self.sobrenome,
            'cpf':self.cpf,
            'email':self.email,
            'rua':self.rua,
            'cep':self.cep,
            'telefone':self.telefone,
            'sexo':self.sexo,
            'data_nascimento':self.data_nascimento
        }