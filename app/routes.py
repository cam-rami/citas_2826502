from . import app, db 
from .models import Cita, Consultorio, Medico, Paciente
from flask import render_template, request, flash, redirect 

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

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html", citas=citas)

#crear ruta tarer medico por id(get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html" , med = medico )

#crear ruta tarer paciente por id(get)
@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html" , pac = paciente )

#crear ruta tarer consultorio por id(get)
@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html" , con = consultorio )

#crear ruta para nuevo medico 
@app.route("/medicos/create" , methods = ["GET" , "POST"])
def create_medico():
    #mostrar el formulario: metodo GET 
    if( request.method == "GET"  ):
        #el usuario ingreso con navegador con http://localhost:5000/medico
        especialidades =[
            "Cardiologo",
            "Pediatria",
            "Oncologia"
        ]
        return render_template("medico_form.html", 
                            especialidades = especialidades )
  
    #####
    ## Cuando el usuario presione el boton guardar
    # los datos del formulario viajan al servidor 
    # utilizar el boton POST
    elif(request.method == "POST"):
        #cuando se presione "guardar"
        #crear un objeto de tipo medico 
        new_medico = Medico(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion =request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)       
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect("/medicos")

    #crear ruta para nuevo paciente
@app.route("/pacientes/create" , methods = ["GET" , "POST"])
def create_paciente():
    #mostrar el formulario: metodo GET 
    if( request.method == "GET"  ):
        #el usuario ingreso con navegador con http://localhost:5000/medico
        return render_template("paciente_form.html")
  
    #####
    ## Cuando el usuario presione el boton guardar
    # los datos del formulario viajan al servidor 
    # utilizar el boton POST
    elif(request.method == "POST"):
        #cuando se presione "guardar"
        #crear un objeto de tipo pacinete
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion =request.form["ni"],
                            altura = request.form["al"],
                            tipo_sangre = request.form["ts"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_paciente)       
        db.session.commit()
        return "paciente registrado"
    
    
@app.route("/consultorios/create" , methods = ["GET" , "POST"])
def create_consultorio():
    #mostrar el formulario: metodo GET 
    if( request.method == "GET"  ):
        #el usuario ingreso con navegador con http://localhost:5000/medico
        return render_template("consultorio_form.html")
   
    elif(request.method == "POST"):
        new_consultorio = Consultorio(numero = request.form["nu"])
        
        db.session.add(new_consultorio)       
        db.session.commit()
        return "consultorio registrado"
    
        #crear ruta para nuevo cita
    
@app.route("/citas/create" , methods = ["GET" , "POST"])
def create_cita():
    #mostrar el formulario: metodo GET 
    if( request.method == "GET"  ):
        #el usuario ingreso con navegador con http://localhost:5000/medico
        return render_template("cita_form.html")
  
    #####
    ## Cuando el usuario presione el boton guardar
    # los datos del formulario viajan al servidor 
    # utilizar el boton POST
    elif(request.method == "POST"):
        #cuando se presione "guardar"
        #crear un objeto de tipo pacinete
        new_cita = Cita(fecha = request.form["fecha"],
                            pacinete = request.form["pac"],
                            medico = request.form["med"],
                            consultorio =request.form["con"],
                            valor = request.form["val"],
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_cita)       
        db.session.commit()
        return "cita registrado"
    
@app.route("/medicos/update/<int:id>" , methods=["POST" , "GET"])
def update_medico(id):
    especialidades =[
            "Cardiologo",
            "Pediatria",
            "Oncologia"
        ]  
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html",
                           medico_update = medico_update,
                           especialidades = especialidades)
    elif(request.method == "POST"):
        medico_update.nombre = request.form["nombre"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return medico_update.nombre
    
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")    
    