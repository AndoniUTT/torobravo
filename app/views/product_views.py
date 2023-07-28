from flask import Blueprint, render_template, redirect, url_for, flash, request

from models.products import Product 

from forms.product_forms import UpdateProductForm, CreateProductForm

product_views = Blueprint('product', __name__)

@product_views.route('/products/')
def producto():
    producto = Product.get_all()
    return render_template('products/products.html',
                           producto=producto)

@product_views.route('/products/create/', methods=('GET', 'POST'))
def create_prod():
    form = CreateProductForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        stock = form.stock.data
        pro = Product(name, price, stock)
        pro.save()
        return redirect(url_for('product.products'))
    return render_template('products/create_prod.html', form=form)

@product_views.route('/products/<int:id>/update/', methods=('GET', 'POST'))
def update_prod(id):
    form = UpdateProductForm()
    pro = Product.get(id)
    if form.validate_on_submit():
        pro.name = form.name.data
        pro.price = form.price.data
        pro.stock = form.stock.data
        pro.save()
        return redirect(url_for('product.products'))
    form.name.data = pro.name
    form.price.data = pro.price
    form.stock.data = pro.stock
    return render_template('products/create_prod.html', form=form )

@product_views.route('/products/<int:id>/delete/', methods=('POST',))
def delete_prod(id):
    #Obtener Cat desde id
    pro = Product.get(id)
    pro.delete()
    #Enviar datos a form
    return redirect(url_for('product.products'))