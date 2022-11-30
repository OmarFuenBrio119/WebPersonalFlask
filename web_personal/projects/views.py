#### imports ####
from flask import render_template, request, Blueprint

project_blueprint = Blueprint('project', __name__)

############# TODO: List Project ######################
@project_blueprint.route('/list')
def list():
    return render_template('project/list.html')

############# TODO: Show Project ######################
@project_blueprint.route('/<project_id>')
def show(project_id=None):
    if project_id is None:
        return render_template('project/list.html')
    return render_template('project/show.html', project_id=project_id)
   
############# TODO: Create ######################
@project_blueprint.route('/new')
def new():
    return render_template('project/new.html')

############# TODO: Update ######################


############# TODO: Delete ######################