from flask import Blueprint, render_template, redirect, url_for, abort, session

from models.products import Product 

from forms.product_forms import UpdateProductForm, CreateProductForm

from models.products import Product
from models.categories import Category

from utils.file_handler import save_image

product_views = Blueprint('product', __name__)

@product_views.route('/products/')
@product_views.route('/products/<int:page>/')
def home(page=1):
    limit = 3
    products = Product.get_all(limit=limit, page=page)
    total_products = Product.count()
    pages = total_products // limit
    user = session.get("user")
    return render_template('products/product.html', products=products, pages=pages, user=user)

@product_views.route('/products/create/', methods=('GET', 'POST'))
def create():
    form = CreateProductForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        stock = form.stock.data
        size = form.size.data
        category_id = form.category_id.data
        f = form.image.data
        image=""
        if f:
            image = save_image(f, 'images/products')
        product = Product(name=name,
                          price=price,
                          stock=stock,
                          size=size,
                          category_id=category_id,
                          image=image)
        product.save()
        return redirect(url_for('product.home'))

    return render_template('products/create_prod.html', form=form)

@product_views.route('/products/<int:id>/update/', methods=('GET', 'POST'))
def update_prod(id):
    form = UpdateProductForm()
    categories = Category.get_all()
    cats = [(-1, '')]
    for cat in categories:
        cats.append((cat.id, cat.category))
    form.category_id.choices = cats
    product = Product.get(id)
    if product is None:
        abort(404)
    if form.validate_on_submit():
        product.name = form.name.data
        product.size = form.size.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.category_id = form.category_id.data
        f = form.image.data
        if f:
            image = save_image(f, 'images/products')
            product.image = image
        product.save()
        return redirect(url_for('product.home'))
    form.name.data = product.name
    form.size.data = product.size
    form.price.data = product.price
    form.stock.data = product.stock
    form.category_id.data = product.category_id
    image = product.image
    return render_template('products/create_prod.html', form=form, image=image)

@product_views.route('/products/<int:id>/detail/')
def detail(id):
    product = Product.get(id)
    if product is None: abort(404)
    cat = Category.get(product.category_id)
    return render_template('products/details.html', product=product, cat=cat)

@product_views.route('/product/<int:id>/delete/', methods=['POST'])
def delete(id):
    product = Product.get(id)
    if product is None: abort(404)
    product.delete()
    return redirect(url_for('product.home'))