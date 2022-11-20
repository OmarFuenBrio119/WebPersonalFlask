from flask import Flask, render_template, request

app = Flask(__name__)

######## Rutas Publicas ##########
@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/portfolio')
def portfolio():
     projects = [
        {
            'name': 'Primer proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful,   warm....,',
            'image': 'img/home-bg.jpg',
            'url': 'https://www.google.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        },
                ]
     return render_template('public/portfolio.html', projects=projects)

########### RUTAS ##################


@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/auth/acesso')
def acesso():
    return render_template('auth/acesso.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome(): 
    email = request.form['mail']
    password = request.form['password']
    access = { 'email': email}

    return render_template('admin/index.html', user_access=access)

if __name__ == '__main__':
    app.run(debug=True)