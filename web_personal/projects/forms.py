####### IMports
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField, TextAreaField, FileField, URLField)
from wtforms.validators import DataRequired, URL, Length
from flask_wtf.file import file_allowed

class FormProjectBase(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=10, max=50)])
    description = TextAreaField('Descripcion', validators=[DataRequired()])
    url = URLField('URL', validators=[DataRequired(), URL()])
    image = FileField('Imagen', validators=[DataRequired(), file_allowed(['jpg','png'])])

class NewProjectForm(FormProjectBase): 
    submit = SubmitField('Crear')

class UpdateProjectForm(FormProjectBase):
    submit = SubmitField('Actualizar')