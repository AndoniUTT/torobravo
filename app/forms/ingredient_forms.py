from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateIngredientForm(FlaskForm):
    name = StringField('Nombre', 
                           validators=[DataRequired()])
    marca = TextAreaField('Marca',
                                validators=[DataRequired()])
    size = TextAreaField('Presentacion',
                                validators=[DataRequired()])
    stock = StringField('Existencia',
                                validators=[DataRequired()])
    submit = SubmitField('Guardar')
    
class UpdateIngredientForm(FlaskForm):
    name = StringField('Nombre', 
                           validators=[DataRequired()])
    marca = TextAreaField('Marca',
                                validators=[DataRequired()])
    size = TextAreaField('Presentacion',
                                validators=[DataRequired()])
    stock = StringField('Existencia',
                                validators=[DataRequired()])
    submit = SubmitField('Guardar')