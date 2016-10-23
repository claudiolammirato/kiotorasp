from flask import Blueprint, render_template

rasp = Blueprint('rasp', __name__,
                        template_folder='templates')

@rasp.route('/')
def index():
    return render_template('index.html')