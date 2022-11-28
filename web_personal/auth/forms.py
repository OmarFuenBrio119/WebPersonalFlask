from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, EmailField, 
                    IntegerField, RadioField, SelectField, TextAreaField)
from wtforms.validators import DataRequired, Email


############# Formularios de WTF ###############

class LoginForm(FlaskForm):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')


class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellidos', validators=[DataRequired()])
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    phone = IntegerField('Telefono', validators=[DataRequired()])
    is_married = RadioField('Estado Civil', choices=[('True', 'Casado'),('False', 'Soltero')])
    gender = SelectField('Genero', choices=[('male', 'Masculino'),('female', 'Femenino'),('other', 'Otro')])
    submit = SubmitField('Registrar')
