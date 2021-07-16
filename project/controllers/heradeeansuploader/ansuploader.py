from flask import Blueprint, render_template

bp = Blueprint('ansupload', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')
