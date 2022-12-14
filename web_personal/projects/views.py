#### imports ####
from flask import render_template, request, Blueprint, redirect, url_for, flash

from .forms import NewProjectForm
from .image_handler import add_image
from db.db_connection import get_connection

project_blueprint = Blueprint('project', __name__)

#### localhost:5000/projects/list ####
#### localhost:5000/project/34 ####
#### localhost:5000/project/new ####
#### localhost:5000/project/34/edit ####
#### localhost:5000/project/34/delete ####

############# TODO: List Project ######################
@project_blueprint.route('/list')
def list():
        projects = [
        {
            'name': 'Primer proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/home-bg.jpg',
            'url': 'https://www.google.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        },
        {
            'name': 'Segundo proyecto', 
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'https://www.xataka.com',
        }
    ]
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM project"
            cursor.execute(sql)
            projects = cursor.fetchall()
        return render_template('project/list.html', projects=projects)


########## TODO: Show Project ##########
@project_blueprint.route('/<project_id>')
def show(project_id=None):
    return render_template('project/show.html', project_id=project_id)
    
########## TODO: Create New Project ##########
@project_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = NewProjectForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        url = form.url.data
        image = add_image(form.image.data)

        conn = get_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO project (name, description, url, image)"
            sql += f"VALUES ('{name}', '{description}', '{url}', '{image}')" 
            cursor.execute(sql)
            conn.commit()
            flash('Proyecto creado correctamente')
            return redirect(url_for('project.list'))


    return render_template('project/new.html', form=form)

########## TODO: Update a Project ##########
@project_blueprint.route('/<project_id>/edit')
def edit(project_id):
    return "Edit Page"


########## TODO: Delete a Project #########
@project_blueprint.route('/<project_id>/delete')
def delete(project_id):
    return "Delete Page"