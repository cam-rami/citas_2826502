#necesitamos a sqLAlchemy:
#Definit los atributos de objeto
#pero con tipos traducidos a SQl y mysql
from app import db

class Medico(db.modelo):
    id = db.Column(db.Integer, primry_key = True )
    nombre = db.Column(db.String(120), nullable = True)
    apellido = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))