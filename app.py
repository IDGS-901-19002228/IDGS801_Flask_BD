from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from config import DevelomentConfig
from flask_wtf.csrf import CSRFProtect
from models import Alumnos, db

from flask import Flask, render_template, request, flash
import forms
from resistencias import Resistencia

app=Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf= CSRFProtect()

@app.route("/", methods=["GET","POST"])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.email.data)
       #Realizar el insert en la bd
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('index.html',form = create_form)

@app.route("/ABCompleto",methods=['GET','POST'])
def ABCompleto():
    create_form=forms.UserForm(request.form)
    #Select * from alumnos
    alumnos=Alumnos.query.all()
    return render_template('ABCompleto.html',form=create_form,alumnos=alumnos)

@app.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.correo
        
    if request.method=='POST':
        #Select * from alumnos where id==id
        id = create_form.id.data
        alum2=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        
        alum2.nombre=create_form.nombre.data
        alum2.apellidos=create_form.apellidos.data
        alum2.email=create_form.email.data
        db.session.add(alum2)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('modificar.html',form=create_form)


@app.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.correo
        
    if request.method=='POST':
        id = create_form.id.data
        alum2=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum2.nombre=create_form.nombre.data
        alum2.apellidos=create_form.apellidos.data
        alum2.email=create_form.email.data
        db.session.delete(alum2)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('eliminar.html',form=create_form)

@app.route("/resistencia", methods=['GET', 'POST'])
def resistencia():
    resist = Resistencia()
    res = {}
    banda1 = ''
    banda2 = ''
    multiplicador = ''
    tolerancia = ''
    resistencia = forms.ResistenciaForm(request.form)
    if request.method == 'POST' and resistencia.validate():
        banda1 = resist.setColor(resistencia.banda1.data)
        banda2 = resist.setColor(resistencia.banda2.data)
        multiplicador = resist.setColor(resistencia.multiplicador.data)
        tolerancia = resist.setTolerancia(resistencia.tolerancia.data)
        res = resist.calcular(resistencia)
        flash('Operacion realizada con exito', 'success')
    return render_template('resistencia.html', form=resistencia, banda1=banda1, banda2=banda2, multiplicador=multiplicador, tolerancia=tolerancia, res=res)


if __name__ =='__main__':
    csrf.init_app(app) #al iniciar tiene seguridad crsf
    db.init_app(app) #iniciar la conexion a la base de datos 
    with app.app_context(): #verifica si se hizo la conexion y crea las tablas 
        db.create_all()
    app.run(port=3000)

