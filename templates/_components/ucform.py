from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length


class UcForm(FlaskForm):
    mysearch = StringField('Palavra-chave: ', validators=[Length(max=80)])
