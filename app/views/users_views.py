from flask import Blueprint, render_template

from forms.users_forms import CreateUserForm

user_views = Blueprint('user', __name__)

@user_views.route('/users/create/')
def create_user():
    form = CreateUserForm()
    return render_template('user/create_user.html',
                           form=form)