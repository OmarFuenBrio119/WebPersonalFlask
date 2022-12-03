####### IMports
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField, TextAreaField, FileField, URLField)
from wtforms.validators import DataRequired, Email

class NewProjectForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripcion', validators=[DataRequired()])
    url = URLField('URL', validators=[DataRequired()])
    image = FileField('Imagen', validators=[DataRequired()])
    submit = SubmitField('Crear')