from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateProductForm(FlaskForm):
    name = StringField('Nombre', 
                           validators=[DataRequired()])
    price = TextAreaField('Precio',
                                validators=[DataRequired()])
    stock = StringField('Stock',
                                validators=[DataRequired()])
    submit = SubmitField('Guardar')
    
class UpdateProductForm(FlaskForm):
    name = StringField('Nombre', 
                           validators=[DataRequired()])
    price = TextAreaField('Precio',
                                validators=[DataRequired()])
    stock = StringField('Stock',
                                validators=[DataRequired()])
    submit = SubmitField('Guardar')