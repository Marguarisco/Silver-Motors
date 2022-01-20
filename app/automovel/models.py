from app.models import BaseModel, db


class Automovel(BaseModel):
    __abstract__ = True

    placa = db.Column(db.String(10), unique=True, index=True)
    modelo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    cor = db.Column(db.String(100))
    valor = db.Column(db.Float)
    ipva = db.Column(db.Float)
    quilometragem = db.Column(db.Float)
    disponivel = db.Column(db.String)

    




    