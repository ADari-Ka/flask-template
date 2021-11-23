from flask import Blueprint, render_template

example_blueprint = Blueprint('example', __name__, template_folder='templates')


@example_blueprint.route('/')
@example_blueprint.route('/index')
def index():
    return render_template('index.html')
