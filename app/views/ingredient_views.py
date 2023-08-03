from flask import Blueprint, render_template, redirect, url_for, flash, request, session

from models.ingredients import Ingredient 

from forms.ingredient_forms import UpdateIngredientForm, CreateIngredientForm

from utils.file_handler import save_image

ingredient_views = Blueprint('ingredient', __name__)

@ingredient_views.route('/ingredients/')
def ingredients():
    ingredients = Ingredient.get_all()
    user = session.get("user")
    return render_template('ingredients/ingredient.html',
                           ingredients=ingredients, user=user)

@ingredient_views.route('/ingredients/create/', methods=('GET', 'POST'))
def create_ingre():
    form = CreateIngredientForm()
    if form.validate_on_submit():
        name = form.name.data
        marca = form.marca.data
        size = form.size.data
        stock = form.stock.data
        f = form.image.data
        image = ""
        if f:
            image = save_image(f, 'images/ingredients')
        ing = Ingredient(name=name, 
                          marca=marca,
                          size=size,
                          stock=stock,
                          image=image)
        ing.save()
        return redirect(url_for('ingredient.ingredients'))
    return render_template('ingredients/create_ingre.html', form=form)

@ingredient_views.route('/ingredients/<int:id>/update/', methods=('GET', 'POST'))
def update_ingre(id):
    form = UpdateIngredientForm()
    ing = Ingredient.get(id)
    if form.validate_on_submit():
        ing.name = form.name.data
        ing.marca = form.marca.data
        ing.size = form.size.data
        ing.stock = form.stock.data
        ing.save()
        return redirect(url_for('ingredient.ingredients'))
    form.name.data = ing.name
    form.marca.data = ing.marca
    form.size.data = ing.size
    form.stock.data = ing.stock
    return render_template('ingredients/create_ingre.html', form=form )

@ingredient_views.route('/ingredients/<int:id>/delete/', methods=('POST',))
def delete_ingre(id):
    #Obtener Cat desde id
    ing = Ingredient.get(id)
    ing.delete()
    #Enviar datos a form
    return redirect(url_for('ingredient.ingredients'))