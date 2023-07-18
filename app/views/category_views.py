from flask import Blueprint, render_template, redirect, url_for, flash, request

from models.categories import Category 

from forms.category_forms import UpdateCategoryForm, CreateCategoryForm

category_views = Blueprint('category', __name__)

@category_views.route('/categories/')
def categories():
    categories = Category.get_all()
    return render_template('categories/categories.html',
                           categories=categories)


@category_views.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    form = CreateCategoryForm()
    if form.validate_on_submit():
        category = form.category.data
        description = form.description.data
        cat = Category(category, description)
        cat.save()
        return redirect(url_for('category.categories'))
    return render_template('categories/create_cat.html', form=form)

@category_views.route('/categories/<int:id>/update/', methods=('GET', 'POST'))
def update_cat(id):
    form = UpdateCategoryForm()
    cat = Category.get(id)
    if form.validate_on_submit():
        cat.category = form.category.data
        cat.description = form.description.data
        cat.save()
        return redirect(url_for('category.categories'))
    form.category.data = cat.category
    form.description.data = cat.description
    return render_template('categories/create_cat.html', form=form )

@category_views.route('/categories/<int:id>/delete/', methods=('POST',))
def delete_cat(id):
    #Obtener Cat desde id
    cat = Category.get(id)
    cat.delete()
    #Enviar datos a form
    return redirect(url_for('category.categories'))