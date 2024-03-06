from . import app 
from .models import Consultorio, Medico, Paciente
from flask import render_template

#crear ruta para ver los listados los medicos 
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html", medicos=medicos )

#crear ruta para ver los listados los pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html", pacientes= pacientes)

#crear ruta para ver los listados los consultorios
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html", consultorios=consultorios)
