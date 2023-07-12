from flask import Blueprint, render_template, redirect, url_for, flash, request

from models.categories import Category 

category_views = Blueprint('category', __name__)

@category_views.route('/categories/')
def categories():
    categories = Category.get_all()
    return render_template('categories/categories.html',
                           categories=categories)


@category_views.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        if not category:
            flash('Debes ingresar una Categoría')
        elif not description:
            flash('Debes ingresar una descripcion')
        else:    
            cat = Category(category, description)
            cat.save()
            return redirect(url_for('category.categories'))
    return render_template('categories/create_cat.html')

@category_views.route('/categories/<int:id>/update/')
def update_cat(id):
    #Obtener Cat desde id
    #Enviar datos a form
    return "Lo vamos a Actualizar"

@category_views.route('/categories/<int:id>/delete/')
def delete_cat(id):
    #Obtener Cat desde id
    cat = Category.get(id)
    cat.delete()
    #Enviar datos a form
    return redirect(url_for('category.categories'))