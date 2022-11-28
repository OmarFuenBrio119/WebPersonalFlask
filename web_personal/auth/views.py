#### imports flask #######
from flask import render_template, Blueprint, redirect, url_for
from db.db_connection import get_connection
####### imports WTF ####
from .forms import LoginForm, RegisterForm
auth_blueprint = Blueprint('auth', __name__)

########### RUTAS Login ##################

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        phone = form.phone.data
        is_married = form.is_married.data
        gender = form.gender.data

        #return str([name, last_name, email, password, phone, is_married, gender])
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (name, last_name, email, password, phone, is_married, gender)"
            sql += f"VALUES ('{name}', '{last_name}', '{email}', '{password}', '{phone}', '{is_married}','{gender}')" 
            cursor.execute(sql)
            conn.commit()
            return redirect(url_for('auth.acesso'))
            

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

