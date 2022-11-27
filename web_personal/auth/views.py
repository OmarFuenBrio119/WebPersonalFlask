#### imports flask #######
from flask import render_template, Blueprint

from db.db_connection import get_connection
####### imports WTF ####
from .forms import LoginForm, RegisterForm

auth_blueprint = Blueprint('auth', __name__)

########### RUTAS Login ##################


@auth_blueprint.route('/register')
def register():
    form = RegisterForm()

    ########Validar ususRio ########

    #conn = get_connection()
    #with conn.cursor() as cursor:
    #  cursor.execute('SELECT * FROM users')
    #  users = cursor.fetchall()
    #   return render_template('auth/register.html', form=form, users=users)

    return render_template('auth/register.html', form=form)






@auth_blueprint.route('/acesso', methods=['GET', 'POST'])

def acesso():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        ########

        return render_template('admin/index.html', email=email)

    return render_template('auth/acesso.html', form=form)

