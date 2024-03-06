#####necesitamos a SQLALchemy:
####Definir los atributos de objecto
####Pero con tipos traducibles  a SQL y mysql
from app import db 
from datetime import datetime

class Medico(db.Model):
    
    __tablename__="medicos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellidos = db.Column(db.String(120), nullable = True) 
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))
    
    citas = db.relationship("Cita", backref = "medico" )
    
class Paciente(db.Model):
        
    __tablename__="pacientes"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellidos = db.Column(db.String(120), nullable = True) 
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    tipo_sangre = db.Column(db.String(2))
    
    citas = db.relationship("Cita", backref = "paciente" )

class Consultorio(db.Model):
    
    __tablename__="consultorios"
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)
    
    citas = db.relationship("Cita", backref = "consultorio" )
    
class Cita(db.Model):
    
    __tablename__="citas" 
    id = db.Column(db.Integer, primary_key =True)
    fecha = db.Column(db.DateTime,default =datetime.utcnow)
    paciente_id = db.Column (db.Integer,db.ForeignKey("pacientes.id"))
    medico_id = db.Column (db.Integer,db.ForeignKey("medicos.id"))
    consultorio_id = db.Column (db.Integer,db.ForeignKey("consultorios.id")) 
    valor = db.Column(db.Integer)
                     
                     
                     
                            

"""from app import app, db
>>> app.app_context().push()
>>> from app.models import Medico,Paciente,Consultorio,Cita
    m1 = Medico(nombre="paola",apellidos="rozio",tipo_identificacion="CC", numero_identificacion=2555856,registro_medico=2589,especialidad="pediatra") 
>>> m2 = Medico(nombre="laura",apellidos="gomez",tipo_identificacion="CC", numero_identificacion=3566588,registro_medico=9685,especialidad="urologo")  
>>> db.session.add(m1)
>>> db.session.add(m2) 
>>> db.session.commit()
>>> p1 = Paciente(nombre="pedro",apellidos="picapiedra",tipo_identificacion="CC",numero_identificacion=25658899,altura=180,tipo_sangre="O-")
>>> p2 = Paciente(nombre="laura",apellidos="gonzales",tipo_identificacion="CC",numero_identificacion=95258695,altura=150,tipo_sangre="O+")   
>>> p3 = Paciente(nombre="santiago",apellidos="ruiz",tipo_identificacion="CC",numero_identificacion=95585885,altura=165,tipo_sangre="B+")  
>>> db.session.add(p1)  
>>> db.session.add(p2) 
>>> db.session.add(p3) 
>>> db.session.commit()
>>> c1 =  Consultorio(numero=106)
>>> c2 =  Consultorio(numero=109) 
>>> c3 =  Consultorio(numero=208) 
>>> c4 =  Consultorio(numero=212) 
>>> db.session.add(c1)  
>>> db.session.add(c2) 
>>> db.session.add(c3) 
>>> db.session.add(c4) 
>>> db.session.commit()
>>> db.session.rollback()
>>> from datetime import datetime
>>> fecha1 = datetime(2024,5,20)
>>> fecha2 = datetime(2024,5,25) 
>>> fecha3 = datetime(2024,5,15) 
>>> fecha4 = datetime(2024,5,10) 
>>> cita1 = Cita(fecha=fecha1,paciente_id=p1,medico_id=m2,consultorio_id=c4,valor=3500)
>>> cita2 = Cita(fecha=fecha3,paciente_id=p3,medico_id=m1,consultorio_id=c2,valor=6000) 
>>> cita3 = Cita(fecha=fecha2,paciente_id=p2,medico_id=m1,consultorio_id=c1,valor=5500) 
>>> cita4 = Cita(fecha=fecha4,paciente_id=p1,medico_id=m2,consultorio_id=c3,valor=10000) 
>>> db.session.add(cita1)                                                                
>>> db.session.add(cita2) 
>>> db.session.add(cita3) 
>>> db.session.add(cita4) 
>>> db.session.commit() 

"""