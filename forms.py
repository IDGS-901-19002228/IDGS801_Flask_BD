from wtforms import Form
from wtforms import  StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

from wtforms import SubmitField, SelectField
from flask_wtf import FlaskForm

from wtforms.fields import RadioField


class UserForm(Form):
    id =IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos') 
    email = EmailField('correo')
    
class ResistenciaForm(FlaskForm):
    banda1 = SelectField('Banda 1', choices=[('0', 'Negro'), 
                                                  ('1', 'Cafe'), 
                                                  ('2', 'Rojo'), 
                                                  ('3', 'Naranja'), 
                                                  ('4', 'Amarillo'), 
                                                  ('5', 'Verde'), 
                                                  ('6', 'Azul'), 
                                                  ('7', 'Morado'), 
                                                  ('8', 'Gris'), 
                                                  ('9', 'Blanco')], 
                              default='0')
    banda2 = SelectField('Banda 2', choices=[('0', 'Negro'), 
                                                  ('1', 'Cafe'), 
                                                  ('2', 'Rojo'), 
                                                  ('3', 'Naranja'), 
                                                  ('4', 'Amarillo'), 
                                                  ('5', 'Verde'), 
                                                  ('6', 'Azul'), 
                                                  ('7', 'Morado'), 
                                                  ('8', 'Gris'), 
                                                  ('9', 'Blanco')], 
                              default='0')
    multiplicador = SelectField('Multiplicador', choices=[('0', 'Negro'), 
                                                  ('1', 'Cafe'), 
                                                  ('2', 'Rojo'), 
                                                  ('3', 'Naranja'), 
                                                  ('4', 'Amarillo'), 
                                                  ('5', 'Verde'), 
                                                  ('6', 'Azul'), 
                                                  ('7', 'Morado'), 
                                                  ('8', 'Gris'), 
                                                  ('9', 'Blanco')], 
                              default='0')    
    tolerancia = RadioField('Tolerancia', choices=[('1', 'Dorado 5%'), ('2', 'Plata 10%')], default='1')
    submit = SubmitField('Calcular')