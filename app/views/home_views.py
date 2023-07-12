from flask import Blueprint, render_template

home_views = Blueprint('home', __name__)

@home_views.route('/')
@home_views.route('/home/')
def home():
    return render_template('home/home.html')

@home_views.route('/about/')
def about():
    return render_template('home/about.html')

@home_views.route('/contact/')
def contact():
    return render_template('home/contact.html')